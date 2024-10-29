
from libreria import pedir_numero

def calcular_tabla(num: int):

    for i in range (11):
        total = num * i
    return total

def main():
    num = pedir_numero()
    
    for i in range(num+1):
        total = calcular_tabla(i)
        print(f'{num} x {i} = {total}')

if __name__ == '__main__':
    main()