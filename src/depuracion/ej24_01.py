
def ordenar(a):
    """
    Ordena una lista de números en orden ascendente usando el algoritmo de burbuja.

    Args:
        a (list): La lista de números a ordenar
    
    Returns:
        a: La lista ordenada en orden ascendente
    """
    n = len(a) # Longitud de la lista a ordenar

    for i in range(n):
        ordenado = True
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                ordenado = False

        if ordenado:
            break
    return a

def main():
    """
    Funcion principal que define una lista de ejemplo, la ordena y muestra el resultado.
    """
    a = [8, 4, 1, 19, 14]
    print(ordenar(a))

if __name__ == '__main__':
    main()