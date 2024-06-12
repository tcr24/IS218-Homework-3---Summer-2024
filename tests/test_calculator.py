import pytest
from faker import Faker
from calculator.calculator import Calculator

fake = Faker()

def test_add():
    a = fake.random_number()
    b = fake.random_number()
    assert Calculator.add(a, b) == a + b

def test_subtract():
    a = fake.random_number()
    b = fake.random_number()
    assert Calculator.subtract(a, b) == a - b

def test_multiply():
    a = fake.random_number()
    b = fake.random_number()
    assert Calculator.multiply(a, b) == a * b

def test_divide():
    a = fake.random_number()
    b = fake.random_number()
    assert Calculator.divide(a, b) == a / b

def test_divide_by_zero():
    a = fake.random_number()
    with pytest.raises(ValueError):
        Calculator.divide(a, 0)

def test_get_last_calculation():
    a = fake.random_number()
    b = fake.random_number()
    Calculator.add(a, b)
    assert Calculator.get_last_calculation() == ('add', a, b, a + b)

def test_clear_history():
    Calculator.clear_history()
    assert Calculator.history == []
