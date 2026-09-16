"""Unit tests for app.py to demonstrate SonarQube coverage reporting."""

import pytest

from app import add, subtract, multiply, divide, power, average, is_even, factorial


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(6, 7) == 42
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(20, 4) == 5
    assert divide(9, 3) == 3


def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        divide(5, 0)


def test_power():
    assert power(2, 8) == 256
    assert power(5, 0) == 1


def test_average():
    assert average([10, 20, 30, 40]) == 25
    assert average([5]) == 5


def test_average_empty_raises():
    with pytest.raises(ValueError):
        average([])


def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False


def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1


def test_factorial_negative_raises():
    with pytest.raises(ValueError):
        factorial(-1)
