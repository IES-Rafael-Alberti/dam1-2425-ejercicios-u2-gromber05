
from libreria import pedir_numero

def comprobar_cero(num):
    if num == 0:
        return True
    else:
        return False
    
def comprobar_negativo(num):
    if num < 0:
        return True
    else:
        return False

    
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