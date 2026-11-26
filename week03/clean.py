"""
第 22 天 · 第三周收尾：把散着的脚本整理成「函数 + 参数 + 日志」

怎么跑（在本文件所在目录，也就是 week03 里）：
    python clean.py                   # 默认读同目录的 jobs.json
    python clean.py 别的文件.json      # 读你指定的文件
    python clean.py 不存在的.json      # 应该优雅报错，不是甩一堆 traceback

它做三件事：
    1. 读一个 jobs.json（BOSS 助手抓下来的岗位数据）
    2. 统计「一共多少条、通过多少条、每条被什么原因挡掉」
    3. 结果打印到屏幕，过程日志写进 clean.log
"""

import json          # 读写 JSON 文件
import logging       # 记日志（比 print 好：带时间、级别，能同时写文件）
import sys           # 拿命令行参数、设置退出码


def load_jobs(path):
    """读 JSON 文件，返回岗位列表；读不到就返回 []（由调用方决定怎么处理）。

    三种「读不到」都要接住，不能让程序崩：
        - 文件不存在        → FileNotFoundError
        - 文件不是合法 JSON → JSONDecodeError
        - 没有 jobs 字段    → 键不存在
    """
    try:
        # with open(...) 结束会自动关闭文件，不用手动 f.close()
        # encoding="utf-8" 必须写：Windows 默认是 GBK，中文会乱码
        with open(path, encoding="utf-8") as f:
            raw = json.load(f)          # load = 从「文件对象」读；loads 才是从字符串读
    except FileNotFoundError:
        logging.error("找不到文件：%s", path)
        return []                        # 空列表 = 告诉调用方「没拿到数据」
    except json.JSONDecodeError as e:
        logging.error("JSON 格式不对：%s", e)
        return []

    # 兼容两种外层结构：
    #   {"at": "...", "jobs": [...]}  → 取 jobs 字段
    #   [...]                          → 本身就是列表
    # 用 .get 而不是 ["jobs"]：键不存在时 .get 返回 None，[] 会抛 KeyError
    rows = raw.get("jobs") if isinstance(raw, dict) else raw

    # None（没这个键）和 []（空列表）都算「没数据」，一起兜住
    if not rows:
        logging.error("文件里没有 jobs 字段，或者 jobs 是空的：%s", path)
        return []

    return rows


def stats(jobs):
    """统计：返回 (总数, 通过数, 拒因分布)。

    注意这个函数只算、不打印 —— 打印是 main 的事。
    「函数返回数据、调用方决定怎么展示」是第 17 天学的分工。
    """
    total = len(jobs)          # 总条数
    passed = 0                 # 通过的条数
    reasons = {}               # 被挡原因 → 出现次数，例如 {"薪资低于 15K": 37}

    for j in jobs:
        # reject 为 None（JSON 的 null）或 ""（空字符串）都表示「通过」。
        # 直接 j.get("reject", "") 有坑：键存在但值是 null 时返回 None 而不是 ""，
        # 所以用 or "" 把 None 也变成空字符串。
        reason = j.get("reject") or ""

        if reason == "":
            passed += 1
        else:
            # 字典累加的标准写法：取不到就当 0，再 +1
            reasons[reason] = reasons.get(reason, 0) + 1

    return total, passed, reasons


def main():
    """程序的入口：串起「读 → 算 → 打印」三步。"""
    # sys.argv[0] 是脚本名，参数从 [1] 开始。
    # 没给参数就用默认文件名，给了就用给的 —— 这样换文件也能跑（今天的过关标准）。
    path = sys.argv[1] if len(sys.argv) > 1 else "jobs.json"

    logging.info("开始处理：%s", path)

    jobs = load_jobs(path)
    if not jobs:
        # 读不到数据就没必要往下算。
        # 退出码 1 = 「我出错了」，这样以后写批处理脚本时能靠它判断成没成。
        logging.error("没有读到任何岗位，退出")
        sys.exit(1)

    total, passed, reasons = stats(jobs)
    logging.info("共 %d 个岗位，通过 %d 个", total, passed)

    # 结果给人看 → 用 print（日志是给排查问题看的，两者用途不同）
    print(f"文件：{path}")
    print(f"总数：{total}")
    print(f"通过：{passed}")
    print("被挡原因：")

    # sorted 按「次数」从多到少排；kv[1] 是 (原因, 次数) 里的次数
    for reason, n in sorted(reasons.items(), key=lambda kv: kv[1], reverse=True):
        print(f"  {n:>3}  {reason}")     # {n:>3} = 数字右对齐占 3 格


if __name__ == "__main__":
    # 只有「直接运行这个文件」时才配置日志；
    # 被别人 import 时不会顺手把 clean.log 建出来。
    logging.basicConfig(
        level=logging.INFO,                                  # INFO 及以上才记（DEBUG 会被过滤）
        format="%(asctime)s %(levelname)s %(message)s",       # 时间 级别 消息
        handlers=[
            logging.FileHandler("clean.log", encoding="utf-8"),  # 写文件，事后可查
            logging.StreamHandler(),                             # 同时打到屏幕，跑的时候能看见
        ],
    )
    main()
