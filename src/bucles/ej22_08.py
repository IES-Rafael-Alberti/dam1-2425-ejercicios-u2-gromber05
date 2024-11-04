
def pedir_numero():
    try:
        num = int(input('Introduzca un número: '))

    except ValueError:
        num = f'\n**ERROR**\n El valor introducido solo puede ser un número\n **ERROR**\n'
    except:
        num = f'\n**ERROR**\n Error desconocido \n**ERROR**\n'
    return num

def triangulo(num: int):
    serie = ''
    for i in reversed(range(1, num+1, 2)):
        i = str(i)
        serie += i + ' '
    return serie

def main():
    num = pedir_numero()
    
    for i in range(0, num+1, 2):
        total = triangulo(i)
        print(f'{total}')

if __name__ == '__main__':
    main()