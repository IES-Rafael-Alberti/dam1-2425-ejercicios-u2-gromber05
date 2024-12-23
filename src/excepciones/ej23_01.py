def preguntar_edad():
    try:
        edad = int(input("¿Cuántos años tienes?: "))

        if edad < 1:
            raise ValueError('La edad introducida no debe ser menor a 1 o negativo')
        if edad > 125:
            raise ValueError('La edad introducida no debe ser mayor a 125')
        else:
            print(mostrar_anios_cumplidos(edad))
    except ValueError as e:
        print(e)

def mostrar_anios_cumplidos(edad: int):
    n = 1
    if edad == 1:
        n = 1
    else:
        while True:
            print(n, end=' ')
            n = n + 1
            if n == edad:
                break
    return n

def main():
    n = preguntar_edad()

if __name__ == '__main__':
    main()
