
def pedir_renta():
    return int(input('¿Cuál es su renta anual?: '))

def comprobar_renta():
    n = pedir_renta()
    if n < 10000:
        print('Debe pagar un 5%')
    if 10000 <= n < 20000:
        print('Debe pagar un 15%')
    if 20000 <= n < 35000:
        print('Debes pagar un 20%')
    if 35000 <= n < 60000:
        print('Debes pagar un 30%')
    if 60000 <= n:
        print('Debes pagar un 45%')
    
def main():
    comprobar_renta()

if __name__ == "__main__":
    main()