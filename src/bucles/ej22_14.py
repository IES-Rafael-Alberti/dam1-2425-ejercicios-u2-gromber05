
from libreria import pedir_numero

def comprobacion(num):
    if num == 0:
        return True
    else:
        return False
    
def main():
    num = pedir_numero()
    suma = 0

    while comprobacion(num) == False:
        suma += num
        num = pedir_numero()

    print(f'La suma de todos los números introducidos es de {suma}')

if __name__ == '__main__':
    main()