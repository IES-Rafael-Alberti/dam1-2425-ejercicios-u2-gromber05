
def preguntar_sexo() -> str:
    n = input("¿Eres hombre o mujer?: ")
    return n.title()

def preguntar_nombre() -> str:
    n = input('¿Cómo te llamas?: ')
    return n.title()

# Corregir si esto está bien o no
def comprobar_grupo(a: str, b: str):
    if a == 'Hombre':
        if 'a' <= b[0] <= 'm':
            return f'Estás en el grupo B'
        else:
            return f'Estás en el grupo A'
    else:
        if  'n' <= b[0] <= 'z':
            return f'Estás en el grupo A'
        else:
            return f'Estás en el grupo B'

def main():
    a = preguntar_nombre()
    b = preguntar_sexo()

    print(comprobar_grupo(a, b))


if __name__ == '__main__':
    main()