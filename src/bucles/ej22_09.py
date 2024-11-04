
def pedir_contraseña():
    return input('Introduzca su contraseña: ')
    
def comprobar_contraseña(contraseña: str):
    comprobacion = False

    while comprobacion == False:

        contraseña = input('Contraseña incorrecta\nIntroduzca una contraseña correcta: ')

        if contraseña == 'contraseña':
            comprobacion = True

    return comprobacion

def main():
    contraseña = pedir_contraseña()
    if comprobar_contraseña(contraseña) == True:
        print(f'Contraseña correcta :)')


if __name__ == '__main__':
    main()


