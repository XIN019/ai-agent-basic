def calculate_average(scores):
    """计算一组成绩的平均分。"""
    total = 0

    for score in scores:
        total = total + score

    average = total / len(scores)
    return average


scores = [78, 92, 85, 66, 88]

average_score = calculate_average(scores)

print("成绩列表：", scores)
print("平均成绩：", average_score)

if average_score >= 90:
    print("整体表现：优秀")
elif average_score >= 80:
    print("整体表现：良好")
elif average_score >= 60:
    print("整体表现：及格")
else:
    print("整体表现：不及格")