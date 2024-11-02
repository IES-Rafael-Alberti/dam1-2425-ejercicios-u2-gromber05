
def preguntar_frase():
    frase = input('Introduzca una frase: ')
    return frase.lower()

def preguntar_letra():
    letra = input('Introduzca una letra: ')
    return letra.lower()

def contar_letras(frase, letra):
    letras = frase.count(letra)
    return letras

def main():
    frase = preguntar_frase()
    letra = preguntar_letra()

    print(f'La cantidad de veces que aparece la letra {letra} es de: {contar_letras(frase, letra)}')

if __name__ == '__main__':
    main()