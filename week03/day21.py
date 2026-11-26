import logging

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s %(levelname)s %(message)s",
    filename="run.log",
    encoding="utf-8",
)

logging.info("程序开始")
try:
    x=1/0
except ZeroDivisionError:
    logging.exception("除零了")

logging.info("程序结束")
print("日志写在 run.log 里了")