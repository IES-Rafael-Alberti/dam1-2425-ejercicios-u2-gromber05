
def pedir_numero():
    try:
        num = int(input('Introduzca un número: '))

    except ValueError:
        num = f'\n**ERROR**\n El valor introducido solo puede ser un número\n **ERROR**\n'
    except:
        num = f'\n**ERROR**\n Error desconocido \n**ERROR**\n'
    return num

def comprobar_cero(num):
    return num == 0
    
def comprobar_negativo(num):
    return num < 0

def main():
    num = pedir_numero()
    suma = 0


    while comprobar_cero(num) == False:
        if comprobar_negativo(num) == False:
            suma += num
            num = pedir_numero()
        else:
            print('El número introducido no puede ser negativo')
            num = pedir_numero()

    print(f'La suma de todos los números introducidos es de {suma}')

if __name__ == '__main__':
    main()