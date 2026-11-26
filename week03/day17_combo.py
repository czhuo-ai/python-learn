"""
第 15-17 天综合：一条能扛住失败的取数流水线

怎么跑：终端里 python week03/day17_combo.py

这段代码把三天的东西叠在一起，各管一件事：
  第 17 天 requests        → 去网上取
  第 16 天 json            → 把文本拆成字典（r.json() 内部就是 json.loads）
  第 15 天 try / except    → 取不到也别死
  外加   def / 参数 / return / for（第 1-4 周学的）把它们组装起来

结构上只有一个原则：函数负责"取一件事"，循环负责"取很多遍"，print 只留在最外面。
"""

import requests


def fetch(name):
    """
    取一个 GitHub 仓库的信息。

    参数 name: 形如 "czhuo-ai/rag-kb" 的仓库全名（用户名/仓库名）
    返回: 永远是字典。
          成功 → {"name": 仓库名, "stars": 星标数, "lang": 语言}
          失败 → {"name": 传入的名字, "error": 原因}
          三条路都返回同样形状的字典，调用的人不用判断类型。
    """
    # f 不能丢：有了它 {name} 才会被替换成真实仓库名；没有它就是四个普通字符
    url = f"https://api.github.com/repos/{name}"

    # try 只包住"可能因为外部原因失败"的部分
    try:
        # timeout 必须写，否则网络卡住会无限等
        r = requests.get(url, timeout=10)

        # 状态码不是异常：404/403 时 requests 照常返回，所以必须自己判
        # 提前 return 的意思是"这条路到此为止"，不会继续往下执行
        if r.status_code != 200:
            return {"name": name, "error": f"HTTP {r.status_code}"}

        # r.json() 把文本变成字典；如果对方返回的不是 JSON，会抛 JSONDecodeError
        # （它属于 RequestException 家族，所以下面的 except 也能接住）
        data = r.json()

        # 用 .get() 而不是 data["x"]：字段缺失时给默认值，不会 KeyError 崩掉
        # language 可能是 null → None，用 or "未知" 换成文字
        return {
            "name": data.get("name"),
            "stars": data.get("stargazers_count", 0),
            "lang": data.get("language") or "未知",
        }

    # 只抓网络相关的异常。抓太宽（比如直接 except:）会把你自己的代码 bug 也吞掉，
    # 到时候程序"不报错但结果不对"，比崩溃更难查
    except requests.RequestException as e:
        return {"name": name, "error": str(e)}


# 主程序：把三个名字依次喂给同一个函数
# 因为失败时返回的是 {"error": ...} 而不是崩溃，所以循环一定能跑完
for repo in ["czhuo-ai/rag-kb", "czhuo-ai/nl2sql-agent", "czhuo-ai/python-learn"]:
    print(fetch(repo))
