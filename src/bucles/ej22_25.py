"""
Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera) y cuántas palabras había. Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.
"""
import os

def borrar_cache():
    os.system('cls')

def pedir_frase():
    frase = input('Introduzca una frase: ')
    return frase

def palabras_a_listas(frase):
    return frase.split()

def contar_letras(frase):
    mayor = 0
    frase_mayor = ''

    for i in frase:
        cantidad_letras = len(i)
        if cantidad_letras > mayor:
            if frase_mayor is not ' ':
                mayor = cantidad_letras
                frase_mayor = i

    return mayor, frase_mayor

def main():
    borrar_cache()
    frase = pedir_frase()

    frase_separada = palabras_a_listas(frase)
    mayor, frase_mayor = contar_letras(frase_separada)

    print(f'La mayor frase ha sido {frase_mayor} y ha contado con {mayor} caractéres')

if __name__ == '__main__':
    main()
        