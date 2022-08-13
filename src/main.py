import os
from logging import getLogger

from fizz.buzz import fizzbuzz

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
logging = getLogger(__name__)
logging.setLevel(LOG_LEVEL)

if __name__ == "__main__":
    for i in range(1, 15):
        ans = fizzbuzz(i)
        logging.info(f"{i} -> {ans}")
