from libreria import pedir_numero

def comprobar_negativo(num):
    if num == -1:
        return True
    elif num < -1:
        raise ValueError('**ERROR** No puedes introducir un valor menor a menos uno')
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