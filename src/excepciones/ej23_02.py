
def pedir_numero():
    num = 0
    while num < 1:
        try:
            num = int(input('Introduzca un número: '))
            if num < 1:
                raise ValueError

        except ValueError:
            print('\n**ERROR**\n El valor introducido solo puede ser un número, además de que tiene que ser igual o mayor a uno\n')
            num = 0

    return num

def bucle(num: int):
    serie = ''
    for i in range(1, num+1, 2):
        i = str(i)
        serie += i + ', '
    serie = serie.rstrip(", ") + '.'

    return serie

def main():
    num = pedir_numero()
    cadena = bucle(num)
    print(f'Años cumplidos: {cadena}')

if __name__ == '__main__':
    main()