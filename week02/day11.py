# ============================================================
# day11.py —— 第 11 天：函数（def / 参数 / return）
#
# 怎么跑：python day11.py
# 函数 = 把一段反复要用的代码起个名字，以后喊名字就行，不用复制粘贴。
# ============================================================

# def 意思是"定义一个函数"：名字叫 average，括号里是它需要的参数 nums。
def average(nums):
    # return 把结果"交回去"，调用它的人才能拿到这个值
    return sum(nums) / len(nums)

def level(score):
    # 走到某个 return 就立刻结束函数，后面的代码不再执行
    if score >= 90:
        return "优秀"
    elif score >= 60:
        return "及格"
    # ⚠️ 原来这里写的是 return 不及格（没有引号）→ 会被当成变量名，
    #    一旦分数低于 60 就报 NameError: name '不及格' is not defined
    #    引号不能丢：文字要用引号包起来
    return "不及格"

def max_of(a, b):
    # 比较两个数，大的那个用 return 交出去
    if a > b:
        return a
    return b

def max_off(a, b, c):
    # 函数里可以调用别的函数：先比 a 和 b，再拿结果和 c 比
    # max_of(max_of(a,b), c) 就是"三个里最大的"
    return max_of(max_of(a, b), c)

scores = [88, 92, 75]

# 调用函数：名字 + 括号 + 参数。average(scores) 返回 (88+92+75)/3 = 85.0
print(average(scores))

# 函数的结果还能直接喂给另一个函数：先算平均 85.0，再判断等级 → "及格"
print(level(average(scores)))

print(max_off(88, 75, 92))

# 三个要记住的点：
#   1) 有 return 函数才会"交出结果"；只 print 不 return 的话，拿到的会是 None
#   2) return 一旦执行，函数立刻结束
#   3) 函数名后面必须有括号，average 是"函数本身"，average(scores) 才是"调用它"
