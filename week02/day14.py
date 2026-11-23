# ============================================================
# day14.py —— 第 14 天：CSV 记账本（本周的收尾项目）
#
# 怎么跑：python day14.py
# 这是第一周结束时的"小项目"：把 3 笔账写进 CSV，再读出来算合计。
# CSV 就是"用逗号隔开的表格"，Excel 能直接打开看。
# ============================================================

import csv    # 读写 CSV 的工具
import os     # 用来判断"文件到底存不存在"

# 文件名放一个变量里，以后要改名只改这一处
FILE = "expenses.csv"

def add(item, amount):
    """记一笔账：item 是项目名，amount 是金额。"""
    # os.path.exists(FILE) → 文件存在返回 True，不存在返回 False
    # not 取反，所以 new = "这是不是一个还没有的新文件"
    new = not os.path.exists(FILE)

    # "a" 追加模式；newline="" 是 csv 模块要求的固定写法，
    # 不写的话 Windows 上每行之间会多出一个空行。
    with open(FILE, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        # 只有第一次新建文件时才写表头，之后追加就不该重复写表头
        if new:
            w.writerow(["项目", "金额"])
        w.writerow([item, amount])

    # 注意这里原来的 {item}{amount} 会粘成"早餐12"，中间补一个空格更好读
    print(f"记上了：{item} {amount} 元")

def show():
    """把账本全部读出来，算合计。"""
    # 文件还没建过就先提示，然后直接返回（return 后面什么都不写 = 结束函数）
    if not os.path.exists(FILE):
        print("还没有任何记录")
        return

    total = 0     # 原来的 tolal 是拼错了，这里改成 total，别的地方也要跟着改
    # "r" 读取；csv.DictReader 会把每一行变成字典：
    #   {"项目": "早餐", "金额": "12"}
    # 所以下面能用 row["项目"]、row["金额"] 取值 —— 这就是第 10 天学的字典
    with open(FILE, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            # {row['项目']:10s} = 占 10 个字符宽度、左对齐（s 表示字符串）
            # {row['金额']:>8s} = 占 8 个字符宽度、右对齐（>），数字对齐才好看
            print(f"{row['项目']:10s}{row['金额']:>8s}")
            # CSV 读出来的金额是字符串 "12"，要 float() 转成数字才能相加
            total += float(row["金额"])

    print("-" * 18)
    # {total:>8.0f} = 右对齐占 8 位、保留 0 位小数（f 表示浮点数）
    print(f"{'合计':10s}{total:>8.0f}")

# if __name__ == "__main__": 的意思是——
#   直接 python day14.py 运行时，下面的代码才执行；
#   如果这个文件被别的文件 import 进去当模块用，下面的代码不会自动跑。
# 这句话是写"既能单独运行、又能被别人引用"的脚本的标准套路。
if __name__ == "__main__":
    add('早餐', 12)
    add('地铁', 6)
    add('咖啡', 18)
    show()

# 提示：每运行一次，上面三笔账就会再追加一遍（这就是你 expenses.csv 里有 9 行、
# 合计 108 元的原因）。想重新开始，就先把 expenses.csv 删掉再跑。
# 下一步（第 15 天之后）会改成"用菜单输入，而不是写死在代码里"。
