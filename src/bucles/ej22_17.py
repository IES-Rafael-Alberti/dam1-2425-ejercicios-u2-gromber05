from libreria import pedir_numero

def separar_numero(num):
    numeros = list(str(num))
    return numeros

def suma_numeros(tupla):
    suma = 0
    for i in tupla:
        i = int(i)
        suma += i
    return suma

def main():
    num = pedir_numero()
    num = separar_numero(num)
    suma = suma_numeros(num)
    print(f'La suma de los números que lo componen es {suma}')

if __name__ == '__main__':
    main()