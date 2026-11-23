# ============================================================
# day13.py —— 第 13 天：文件读写（open / with）
#
# 怎么跑：python day13.py
# 文件名原来叫 "day13,py"（逗号是笔误），已经改成 day13.py。
# 这一天只练一件事：把数据存到硬盘上，下次还在。
# ============================================================

# with open(文件名, 模式, encoding="utf-8") as f:
#   - "w" = 写入，会【先把文件清空】再写（这点最容易踩坑：跑一次就覆盖一次）
#   - encoding="utf-8" 一定要写，否则中文在 Windows 上会变成乱码
#   - with 的作用：代码块结束后自动帮你把文件关掉，不用手动 close()
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("第一行：今天学了文件\n")     # \n 是换行符，不写的话两句话会粘在同一行
    f.write("第二行: 还学了with\n")

# "a" = 追加（append）：在文件末尾接着写，不会清空原来的内容。
# 想保留以前的内容就用 "a"，想重写就用 "w"。
with open("notes.txt", "a", encoding="utf-8") as f:
    f.write("第三行：追加一行\n")

# "r" = 读取。f.read() 一次把整个文件读成一个字符串。
with open("notes.txt", "r", encoding="utf-8") as f:
    text = f.read()
print(text)

print("---按行读---")

# 更常用的读法：直接 for line in f，一行一行地读（大文件也不会撑爆内存）。
# enumerate(..., start=1) 给每行配个行号，从 1 开始。
# line.strip() 去掉行尾的换行符 \n 和多余空格，不然打印出来会多空一行。
with open("notes.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}:{line.strip()}")

# 三个模式记住：w 重写（先清空）、a 追加、r 只读。
# 忘了写 encoding="utf-8"，中文就变问号或乱码。
