def ordenar(a):
    """
    Ordena una lista de números en orden ascendente usando el algoritmo de burbuja.

    Args:
        a (list): La lista de números a ordenar.
    
    Returns:
        a (list): La lista ordenada en orden ascendente.
    """
    n = len(a)  # Longitud de la lista a ordenar.

    for i in range(n):
        # Suponemos que la lista ya está ordenada al inicio de cada repetición.
        ordenado = True
        # Repetimos desde el inicio hasta el último elemento no ordenado.
        for j in range(0, n - i - 1):
            # Si el numero actual es mayor que el siguiente, los cambiamos.
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                # Si hacemos un cambio, significa que la lista aun no está lista.
                ordenado = False
        # Si no se hicieron cambios, podemos considerar que la lista ya está ordenada y la devolvemos
        if ordenado:
            break
    return a

def main():
    """
    Función principal que define la lista a ordenar, la ordena y retorna el resultado.
    """
    a = [8, 4, 1, 19, 14]  # Lista a ordenar.
    print(ordenar(a))  # Llamamos a la función ordenar y retornamos el resultado.


if __name__ == '__main__':
    main()
