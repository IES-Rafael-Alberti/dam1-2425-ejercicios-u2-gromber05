
def preguntar_edad():
    return int(input("¿Cuántos años tienes?: "))

def calcular_precio(n: int) -> str:
    if n < 4:
        return 'Gratis'
    elif 4 <= n < 18:
        return '5€'
    else:
        return '10€'
    
def main():
    n = preguntar_edad()
    print(f'El precio de tu entrada es: {calcular_precio(n)}')

if __name__ == '__main__':
    main()