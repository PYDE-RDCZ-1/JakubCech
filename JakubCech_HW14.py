import pytest
import math

def obsah(x, v):
    S = 0.5 * x * v
    return S


def test_obsah():
    assert obsah(3, 5) == 7.5
    assert obsah(10, 5) == 25
    assert obsah(8, 3) == 12


def obvod(polomer):
    o = round(2 * math.pi * polomer)
    return(o)

def test_obvod():
    assert obvod(5) == 31
    assert obvod(21) == 132
    assert obvod(8) == 50