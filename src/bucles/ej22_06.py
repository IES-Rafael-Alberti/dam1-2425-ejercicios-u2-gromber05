
from libreria import pedir_numero

def bucle(num):
    serie = ''
    for i in range(num):
        serie = serie + '*'
    return serie

def main():
    num = pedir_numero()
    for i in range(1, num + 1):
        print(bucle(i))

if __name__ == '__main__':
    main()