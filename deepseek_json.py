import json
import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    raise RuntimeError("没有读取到 DEEPSEEK_API_KEY。")


client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com",
)


notice = """
通知：本周五下午3点，在教学楼A203召开AI Agent项目会议。
请全体项目成员携带电脑参加。
"""


system_prompt = """
你是一个信息提取助手。

请从用户提供的通知文本中提取信息，并严格输出合法的 JSON。
不要输出 Markdown 代码块，不要输出解释文字。

JSON 格式示例：
{
  "event": "会议名称",
  "date": "日期",
  "time": "时间",
  "location": "地点",
  "participants": "参与人员",
  "requirement": "需要携带或完成的事项"
}
"""


try:
    response = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": notice,
            },
        ],
        response_format={
            "type": "json_object"
        },
        extra_body={
            "thinking": {
                "type": "disabled"
            }
        },
        temperature=0.2,
        max_tokens=500,
        stream=False,
    )

    content = response.choices[0].message.content

    print("模型返回的原始内容：")
    print(content)

    # 验证模型返回内容是否为合法 JSON
    result = json.loads(content)

    print("\njson.loads 解析成功：")
    print(json.dumps(result, ensure_ascii=False, indent=2))

    print("\n会议名称：", result["event"])
    print("会议地点：", result["location"])

except json.JSONDecodeError as error:
    print("模型输出不是合法 JSON：")
    print(error)

except Exception as error:
    print("API 调用失败：")
    print(type(error).__name__)
    print(error)