
def pedir_puntuacion():
    n = None
    while n == None:
        n = float(input('Introduzca su puntuación: '))
    return n

def comprobar_puntuacion(n: float) -> str:
    
    if n == 0.0:
        return f'Inaceptable'
    if n == 0.4:
        return f'Aceptable'
    if n >= 0.6:
        return f'Meritorio'
    else: 
        return None

def main():
    n = pedir_puntuacion()
    while comprobar_puntuacion(n) != None:
        print(f'Tu puntuación ha sido de {n} y tienes una calificación de {comprobar_puntuacion(n)}')
    else: 
        print('No puedes tener la calificación que has introducido')

if __name__ == '__main__':
    main()