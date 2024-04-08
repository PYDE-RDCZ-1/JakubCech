import pytest

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b



def test_subsctract():
    assert substract(3,2) == 1

def test_multiplication():
    assert multiplication(2,3) == 6

def test_division():
    assert division(6, 3) == 2

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (10, -5, 5),
])

def test_add(a, b, expected):
    assert add(a, b) == expected