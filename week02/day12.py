# ============================================================
# day12.py —— 第 12 天：模块（import）与用别人写好的代码
#
# 怎么跑：python day12.py（必须在 week02 文件夹里跑，因为要 import mytools）
# 模块 = 别人（或过去的你）写好的一整份 .py 文件，import 进来就能用。
# ============================================================

# import 模块名：把整个模块拿进来，用的时候写成 模块名.函数名
import random
import datetime

# from 模块 import 函数名：只拿其中某个函数，之后可以直接喊名字
# 注意：mytools 是同一个文件夹里的 mytools.py，这就是"自己写模块"
from mytools import greet, half

# 调用 mytools.py 里的 greet()，返回 f"你好，陈卓"
print(greet("陈卓"))

# 调用 half(10) → 10/2 = 5.0
print(half(10))

# random.randint(1, 6)：随机整数，两边都包含 → 1~6，正好模拟掷骰子
# 每次运行结果都不一样，这就是"随机"
print(random.randint(1, 6))

# datetime.datetime.now() 拿到"现在这一刻"，
# 后面 .strftime("%Y-%m-%d %H:%M") 把它格式化成 2026-11-23 19:30 这种样子
# %Y 年 / %m 月 / %d 日 / %H 时 / %M 分，记住这五个就够用
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

# round(数字, 几位小数)：四舍五入到 2 位 → 3.14
print(round(3.14159, 2))

# 常见坑：报 ModuleNotFoundError: No module named 'mytools'
#   → 说明当前目录不是 week02，或者 mytools.py 不在同一个文件夹里。
