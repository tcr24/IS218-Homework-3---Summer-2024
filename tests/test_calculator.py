import pytest
from calculator.calculator import Calculator

def test_add():
    assert Calculator.add(1, 2) == 3

def test_subtract():
    assert Calculator.subtract(4, 2) == 2

def test_multiply():
    assert Calculator.multiply(2, 3) == 6

def test_divide():
    assert Calculator.divide(6, 2) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        Calculator.divide(1, 0)

def test_get_last_calculation():
    Calculator.add(2, 3)
    assert Calculator.get_last_calculation() == ('add', 2, 3, 5)

def test_clear_history():
    Calculator.clear_history()
    assert Calculator.history == []
