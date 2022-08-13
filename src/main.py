import os
import sys

from loguru import logger

# logging.getLoggerを呼ぶモジュールより先にimportする必要あり
from fizz.buzz import fizzbuzz

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")

logger.remove()
# loggerはグローバルなので他モジュールでimportしても以下の設定が効いた状態になる
FORMAT = "[{time:YYYY-MM-DD HH:mm:ss.SSSZ} {level} {module}:{line}] {message}"
logger.add(sys.stdout, format=FORMAT, level=LOG_LEVEL)

# Colorize
# logger.add(sys.stdout, format="{time} {level} {message}",  level=LOG_LEVEL, colorize=True)

# JSON
# logger.add(sys.stdout, format="{time} {level} {message}",  level=LOG_LEVEL, serialize=True)


if __name__ == "__main__":

    print(__name__)
    for i in range(1, 3 + 1):
        ans = fizzbuzz(i)
        logger.info(f"{i} -> {ans}")

    logger.debug("main debug")
    logger.info("main info")
    logger.warning("main warning")
    logger.error("main error")
