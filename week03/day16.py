"""
第 16 天：json —— 字典和文本之间来回转换

怎么跑：终端里 python week03/day16.py
今天要建立的认识：程序内存里的"字典"没法直接给别人（发网络、存文件、传给别的程序），
必须先变成"一段文本"。这段文本的格式就叫 JSON。

四个函数，记住一句话：带 s 的管字符串（string），不带 s 的管文件。
  json.dumps(字典)      → 字符串       dump s = dump string
  json.loads(字符串)    → 字典         load s = load string
  json.dump(字典, 文件)  → 写进文件
  json.load(文件)       → 读出来变成字典
"""

import json

# 内存里的字典：键是字符串，值是任意类型（数字、列表都行）
data = {
    "name": "陈卓",
    "age": 21,
    "skills": ["Python", "SQL"],
    "city": "深圳",
}

# ── 字典 → 文本 ────────────────────────────────────────────────
# ensure_ascii=False：中文原样输出，不加这个会变成 "\u9648\u5353" 这种转义
# indent=2：每个层级缩进 2 格，人能读；不写就是挤成一整行（机器读没问题，人读很痛苦）
text = json.dumps(data, ensure_ascii=False, indent=2)
print(text)
# 想知道它到底是什么类型，可以临时加一行：print(type(text)) → <class 'str'>


# ── 文本 → 字典 ────────────────────────────────────────────────
# 这一步才拿回"能按名字取格子"的东西。
# 可以试一下：删掉下面这行，改成 print(text["skills"])，
# 会报 TypeError: string indices must be integers —— 因为 text 是字符串，只能按位置取。
back = json.loads(text)
print(back["skills"][0])               # Python：先取 skills 列表，再取第 0 个


# ── 存文件（"w" = write，会先清空原文件）──────────────────────────
# 注意这里是 json.dump（没有 s）：因为它要的是"文件对象" f，不是字符串。
# 写了 dumps 会报 TypeError: dumps() takes 1 positional argument...
# with 的意思是"用完自动关文件"，比手动 f.close() 安全，忘了关也不会锁住文件。
with open("profile.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)


# ── 从文件读回来（"r" = read）────────────────────────────────────
# 同样用 json.load（没有 s），参数是文件对象。
# 如果上面写错了（比如误用 dumps），这里会报 JSONDecodeError: Expecting value ——
# 因为文件被 open(...,"w") 清空后一个字节都没写进去。
with open("profile.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded["city"])                  # 深圳
