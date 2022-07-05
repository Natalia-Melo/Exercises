## To run the tests in this file:
##      pytest
from FizzBuzz5 import processNumber

def test_3_multiple():
    assert processNumber(3) == "Fizz"
    assert processNumber(6) == "Fizz"

def test_5_multiple():
    assert processNumber(5) == "Buzz"
    assert processNumber(10) == "Buzz"


def test_3_and_5_multiple():
    assert processNumber(15) == "FizzBuzz"
    assert processNumber(30) == "FizzBuzz"


def test_7_multiple():
    assert processNumber(7) == "Bang"
    assert processNumber(21) == "FizzBang"
    assert processNumber(105) == "FizzBuzzBang"


def test_11_multiple():
    assert processNumber(11) == "Bong"
    assert processNumber(22) == "Bong"
    assert processNumber(33) == "Bong"
    assert processNumber(44) == "Bong"
    assert processNumber(55) == "Bong"


def test_13_multiple():
    assert processNumber(65) == "FezzBuzz"
    assert processNumber(195) == "FizzFezzBuzz"
    assert processNumber(143) == "FezzBong"
    assert processNumber(3*5*7*13) == "FizzFezzBuzzBang"

def test_17_multiple():
    assert processNumber(255) == "BuzzFizz"


def test_prime_numbers():
    assert int(processNumber(19)) == 19
    assert int(processNumber(23)) == 23
    assert int(processNumber(89)) == 89
    assert int(processNumber(97)) == 97

test_17_multiple()