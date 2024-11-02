
def pedir_numero():
    try:
        num = int(input('Introduzca un número: '))
    
    except ValueError:
        print('\n**ERROR**\n El valor introducido solo puede ser un número')