import logging

# logger = logging.getLogger("app")
logger = logging.getLogger(__name__)


def fizzbuzz(num: int) -> str:
    if num == 1:
        logger.debug("fizzbuzz debug")
        logger.info("fizzbuzz info")
        logger.warning("fizzbuzz warning")
        logger.error("fizzbuzz error")

    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    return str(num)
