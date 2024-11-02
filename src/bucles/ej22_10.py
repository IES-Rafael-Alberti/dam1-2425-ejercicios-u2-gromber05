from libreria import pedir_numero

def calcular_primo(num):
    divisores_num = 0

    for i in range(1, num):
        divisores = num % i
        if divisores == 0:
            divisores_num += 1
    return divisores_num

def main():
    n = pedir_numero()
    if calcular_primo(n) <= 1:
        print(f'El número {n} es primo')
    else:
        print(f'El número {n} no es primo')

if __name__ == '__main__':
    main()