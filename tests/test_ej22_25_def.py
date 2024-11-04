import pytest
from src.bucles.ej22_25 import palabras_a_listas

def test_palabras_a_listas():
    assert palabras_a_listas("Samba do Brasil") == ['Samba', 'do', 'Brasil']
    assert palabras_a_listas("Palazo en los dientes") == ['Palazo', 'en', 'los', 'dientes']
    assert palabras_a_listas("Rayada histórica") == ['Rayada', 'histórica']
    assert palabras_a_listas("Si necesitan más ayuda, que la pidan") == ['Si', 'necesitan', 'más', 'ayuda,', 'que', 'la', 'pidan']
    assert palabras_a_listas("Pedrada en la cabeza") == ['Pedrada', 'en', 'la', 'cabeza']
