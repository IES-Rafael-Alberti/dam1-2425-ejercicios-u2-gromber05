
def pedir_numero():

    try:
        num = int(input('Introduzca un número: '))

    except ValueError:
        print('\n**ERROR**\n La entrada no es correcta')
        num = 0

def main():
    pedir_numero()

if __name__ == '__main__':
    main()