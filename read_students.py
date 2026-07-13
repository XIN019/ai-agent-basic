import json


with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)


total_score = 0

for student in students:
    name = student["name"]
    score = student["score"]

    print(f"{name}:{score} 分")
    total_score += score


average_score = total_score / len(students)

print("学生人数：", len(students))
print("平均成绩：", average_score)


scores = []

for student in students:
    scores.append(student["score"])

highest_score = max(scores)
lowest_score = min(scores)

print("最高成绩：", highest_score)
print("最低成绩：", lowest_score)


summary = {
    "student_count": len(students),
    "average_score": average_score,
    "highest_score": highest_score,
    "lowest_score": lowest_score
}


with open("summary.json", "w", encoding="utf-8") as file:
    json.dump(summary, file, ensure_ascii=False, indent=2)

print("统计结果已保存到 summary.json")