import logging
import logging.config
import os

# logging.getLoggerを呼ぶモジュールより先にimportする必要あり
import config.load_log_config
from fizz.buzz import fizzbuzz

logger = logging.getLogger(__name__)
print(os.environ.get("LOG_LEVEL"))
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
logger.setLevel(LOG_LEVEL)


if __name__ == "__main__":

    print(__name__)
    for i in range(1, 3 + 1):
        ans = fizzbuzz(i)
        logger.info(f"{i} -> {ans}")

    logger.debug("main debug")
    logger.info("main info")
    logger.warning("main warning")
    logger.error("main error")
