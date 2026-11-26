"""
第 15 天：try / except —— 让程序在出错时不崩

怎么跑：终端里 python week03/day15.py
今天要建立的认识：错误不是一个"结果"，而是一个"能被接住的东西"。
接住了 → 程序继续往下跑；没接住 → 程序当场停下（后面的代码一行都不执行）。

三个例子分别演示 Python 里最常见的三种错：
  ValueError          —— 类型对，但值不对（"abc" 转不成数字）
  ZeroDivisionError   —— 除以 0
  FileNotFoundError   —— 文件不存在
"""

# ── 例 1：int() 转不了的时候，抛的是 ValueError ──────────────────
# except 后面写具体的错误类型，意思是"我只接这一种"。
# 如果写成裸的 except:，会把所有错误都吞掉，包括你自己写错变量名那种 bug —— 别那么写。
try:
    n = int("abc")             # 这行执行失败，立刻跳到 except，try 里后面的行不再执行
except ValueError as e:
    print("转换失败:", e)       # e 里是具体原因：invalid literal for int() with base 10: 'abc'


# ── 例 2：除以 0 是 ZeroDivisionError，不是 ValueError ───────────
# 每种错误都有自己的名字，名字不对就接不住（接不住 = 程序崩）。
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("不能除以零:", e)


# ── 例 3：打开一个不存在的文件 ───────────────────────────────────
# 这里文件名故意写错（no_sunch_file.txt），就是为了让 open() 失败。
# 注意 encoding="utf-8" 要写：Windows 默认用 GBK 读文件，中文会乱码。
try:
    open("no_sunch_file.txt", encoding="utf-8")
except FileNotFoundError as e:
    print("文件没找到:", e)


# 走到这一行，说明上面三次都"接住"了。
# 这句话本身就是今天最大的收获：出错并不意味着程序必须死。
print("程序没有崩，继续往下走")


# ── 把 try/except 包进函数：这才是它真正有用的形态 ────────────────
# 单次转换失败无所谓，但如果一整个循环里第 87 条数据是脏的，
# 没有 safe_int 的话，前 86 条白干、程序还崩在那儿。
# 有了它：脏数据变成 0，处理继续。
def safe_int(text):
    """能转就返回数字；转不了返回 0。参数是文本，返回是整数。"""
    try:
        return int(text)       # 正常情况：直接交出去，后面 except 不执行
    except ValueError:
        return 0               # 转不了一律给 0：宁可数据为 0，也不要整批处理崩掉


# "abab" 转不成数字 —— 如果不接住，这里就是个红色的 ValueError
print(safe_int("abab"))
