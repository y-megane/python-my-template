import pytest

from fizz.buzz import fizzbuzz


@pytest.mark.unit
def test_fizzbuzz():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
