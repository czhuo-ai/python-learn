"""
第 17 天：requests —— 从网上的接口取数据

怎么跑：终端里 python week03/day17.py
今天要建立的认识：取回来的东西永远是"文本"，而且随时可能失败（断网/超时/404/限流）。

一条完整的取数链路是这样的四步，每一步都可能出事：
  1. requests.get(url, timeout=10)   发请求（可能断网、可能超时）
  2. r.status_code                   看对方怎么回（200 成功 / 404 没有 / 403 限流）
  3. r.text                          拿到一堆字符（就是"快递单"）
  4. r.json()                        把字符变成字典（内部就是 json.loads）

注意：这个脚本没有写 try/except，所以一旦网络出问题，它会直接崩 —— 
这是故意的，day17_combo.py 才是加了保护的完整版。
"""

import requests

# 这里用的是 GitHub 的公开 API：GET /repos/{owner}/{repo} 返回仓库信息
url = "https://api.github.com/repos/czhuo-ai/rag-kb"

# timeout=10 必须写：不写的话，网络卡住时程序会无限期等下去（假死）
# 它同时管"连接超时"和"读取超时"，单位是秒
r = requests.get(url, timeout=10)

# 状态码是 HTTP 协议里的"结果码"，不是异常，requests 不会因为 404 抛错
#   200 成功 / 404 地址或资源不存在 / 403 被拒绝（这里常见于触发限流）/ 500 对方服务器挂了
print("状态码:", r.status_code)

# r.ok 是 requests 给的便捷属性：状态码 < 400 时为 True
print("是不是 200:", r.ok)

# r.text 是对方返回的原始文本（字符串）。
# 打印出来你会看到 "name":"rag-kb" 这种带引号的样子 —— 那是文本里的字符，不是字典的键
# print(r.text[:200])

# r.json() = json.loads(r.text)：文本 → 字典。名字里的 json 就是第 16 天那个模块
data = r.json()

print("仓库名:", data["name"])
print("星标数:", data["stargazers_count"])

# language 有可能返回 null（仓库里只有 README 时就是 null），
# 到了 Python 变成 None，这里会打印 None 而不报错。
# 更稳的写法：data.get("language") or "未知"
print("语言:", data["language"])
