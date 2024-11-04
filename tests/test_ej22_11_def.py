import pytest
from src.bucles.ej22_11 import separar_frase

def test_separar_frase():
    assert separar_frase("Samba do Brasil") == ['S', 'a', 'm', 'b', 'a', ' ', 'd', 'o', ' ', 'B', 'r', 'a', 's', 'i', 'l']
    assert separar_frase("Palazo en los dientes") == ['P', 'a', 'l', 'a', 'z', 'o', ' ', 'e', 'n', ' ', 'l', 'o', 's', ' ', 'd', 'i', 'e', 'n', 't', 'e', 's']
    assert separar_frase("Rayada histórica") == ['R', 'a', 'y', 'a', 'd', 'a', ' ', 'h', 'i', 's', 't', 'ó', 'r', 'i', 'c', 'a']
    assert separar_frase("Si necesitan más ayuda, que la pidan") == ['S', 'i', ' ', 'n', 'e', 'c', 'e', 's', 'i', 't', 'a', 'n', ' ', 'm', 'á', 's', ' ', 'a', 'y', 'u', 'd', 'a', ',', ' ', 'q', 'u', 'e', ' ', 'l', 'a', ' ', 'p', 'i', 'd', 'a', 'n']
    assert separar_frase("Pedrada en la cabeza") == ['P', 'e', 'd', 'r', 'a', 'd', 'a', ' ', 'e', 'n', ' ', 'l', 'a', ' ', 'c', 'a', 'b', 'e', 'z', 'a']
