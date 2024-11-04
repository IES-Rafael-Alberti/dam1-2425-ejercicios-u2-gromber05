import pytest
from src.bucles.ej22_22 import calcular_par_impar

def test_calcular_par_impar():
    assert calcular_par_impar(1) == False
    assert calcular_par_impar(2) == True
    assert calcular_par_impar(3) == False
    assert calcular_par_impar(4) == True
    assert calcular_par_impar(5) == False