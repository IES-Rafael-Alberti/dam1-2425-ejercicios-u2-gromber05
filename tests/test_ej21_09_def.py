import pytest
from src.condicionales.ej21_09 import calcular_precio

def test_calcular_precio():
    assert calcular_precio(1) == "Gratis"
    assert calcular_precio(4) == "5€"
    assert calcular_precio(6) == "5€"
    assert calcular_precio(18) == "10€"
    assert calcular_precio(20) == "10€"