import pytest
from src.bucles.ej22_15 import comprobar_negativo

def test_comprobar_negativo():
    assert comprobar_negativo(1) == False
    assert comprobar_negativo(4) == False
    assert comprobar_negativo(-1) == True
    assert comprobar_negativo(-3) == True
    assert comprobar_negativo(4) == False