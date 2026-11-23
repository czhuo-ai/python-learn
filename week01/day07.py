name = input("你叫什么名字？")
birth = int(input("你是哪一年出生的？"))
score = int(input("输入你的分数："))

age = 2026 - birth

if score >= 90:
    level = "优秀"
elif score >= 60:
    level = "及格"
else:
    level = "不及格"

print(f"{name}，你今年 {age} 岁，成绩{level}")
if score < 60:
    print("下周重点复习")