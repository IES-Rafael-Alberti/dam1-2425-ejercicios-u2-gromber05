def pedir_numero():
    try:
        num = int(input('Introduzca un número: '))

    except ValueError:
        num = f'\n**ERROR**\n El valor introducido solo puede ser un número\n **ERROR**\n'
    except:
        num = f'\n**ERROR**\n Error desconocido \n**ERROR**\n'
    return num

def comprobar_negativo(num):
    if num == -1:
        return True
    elif num < -1:
        print('**ERROR** No puedes introducir un valor menor a menos uno')
    else:
        return False
    
def main():
    num = pedir_numero()
    suma = 0

    while comprobar_negativo(num) == False:
        suma += num
        num = pedir_numero()

    print(f'La suma de los números introducidos es {suma}')

if __name__ == '__main__':
    main()