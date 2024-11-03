import pytest
from src.bucles.ej22_13 import comprobar

def test_pedir_numero():
    assert comprobar("SaLIR") == True
    assert comprobar("saliur") == False
    assert comprobar("SALIR") == True
    assert comprobar("salir") == True
    assert comprobar("selir") == False