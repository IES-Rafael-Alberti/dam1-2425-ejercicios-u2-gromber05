import pytest
from src.bucles.ej22_03 import bucle

def test_bucle():
    assert bucle(1) == ' 1'
    assert bucle(3) == ' 1, 3' 
    assert bucle(5) == ' 1, 3, 5' 
    assert bucle(8) == ' 1, 3, 5, 7' 
    assert bucle(15) == ' 1, 3, 5, 7, 9, 11, 13, 15'
