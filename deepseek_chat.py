import os

from dotenv import load_dotenv
from openai import OpenAI


# 从当前目录的 .env 文件加载环境变量
load_dotenv()

# 获取 DeepSeek API Key
api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    raise RuntimeError(
        "没有读取到 DEEPSEEK_API_KEY，"
        "请检查 .env 文件名和变量名是否正确。"
    )


# 创建 DeepSeek 客户端
client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com",
)


try:
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {
                "role": "system",
                "content": "你是一名耐心的编程入门老师，回答简洁、准确。",
            },
            {
                "role": "user",
                "content": "请用三句话介绍 Markdown，并给出一个一级标题语法示例。",
            },
        ],
        # 关闭思考模式，以便练习 temperature 参数
        extra_body={
            "thinking": {
                "type": "disabled"
            }
        },
        temperature=0.2,
        max_tokens=300,
        stream=False,
    )

    answer = response.choices[0].message.content

    print("模型回复：")
    print(answer)

    # 查看本次调用的 Token 用量
    if response.usage:
        print("\nToken 使用情况：")
        print("输入 Token：", response.usage.prompt_tokens)
        print("输出 Token：", response.usage.completion_tokens)
        print("总 Token：", response.usage.total_tokens)

except Exception as error:
    print("DeepSeek API 调用失败：")
    print(type(error).__name__)
    print(error)