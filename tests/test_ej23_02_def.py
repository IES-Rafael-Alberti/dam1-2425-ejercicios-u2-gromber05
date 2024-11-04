import pytest
from src.bucles.ej23_02 import triangulo

def test_triangulo():
    assert triangulo(1) == '1 '
    assert triangulo(4) == '3 1 '
    assert triangulo(6) == '5 3 1 '
    assert triangulo(18) == '17 15 13 11 9 7 5 3 1 '
    assert triangulo(20) == '19 17 15 13 11 9 7 5 3 1 '