from libreria import pedir_numero

def bucle(num: int):
    serie = ' '
    for i in range(1, num + 1, 2):
        i = str(i)
        serie += i + ', '
    serie = serie.rstrip(', ')
    return serie

def main():
    n = pedir_numero()
    print(f'{bucle(n)}')

if __name__ == '__main__':
    main()