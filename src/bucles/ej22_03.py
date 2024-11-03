def pedir_numero():
    try:
        num = int(input('Introduzca un número: '))

    except ValueError:
        num = f'\n**ERROR**\n El valor introducido solo puede ser un número\n **ERROR**\n'
    except:
        num = f'\n**ERROR**\n Error desconocido \n**ERROR**\n'
    return num

def bucle(num: int):
    serie = ' '
    for i in range(1, num + 1, 2):
        i = str(i)
        serie += i + ', '
    serie = serie.rstrip(', ')
    return serie

def main():
    n = pedir_numero()
    print(f'{bucle(n)}')

if __name__ == '__main__':
    main()