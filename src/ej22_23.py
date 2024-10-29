import os

def preguntar_libro():
    libro = input('Libro: ')
    libro_total = ''
    contador_espacios = 0

    while libro != '*':
        libro_total += ' ' + libro
        libro = input('Libro: ')

        if libro == '/':
           suma = contar_digitos(libro_total)  
           print(f'Línea completa. Aparecen {suma} dígitos numéricos')
           contador_espacios += 1
           suma = 0
    else:
        print(f'Fin. Se leyeron {contador_espacios} líneas completas.')

def borrar_cache():
    os.system('cls')

def contar_digitos(frase):
    numeros = sum(1 for caracter in frase if caracter.isdigit())
    return numeros

def main():
    borrar_cache()
    libro_total = preguntar_libro()

if __name__ == '__main__':
    main()