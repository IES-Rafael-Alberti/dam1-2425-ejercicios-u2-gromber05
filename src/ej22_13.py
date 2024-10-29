import os

def pedir_palabra():
    mensaje = input('')
    return mensaje

def comprobar(mensaje: str):
    if mensaje.lower() == 'salir':
        return True
    else:
        return False

def main():
    os.system('cls')
    mensaje = pedir_palabra()
    comprobacion = comprobar(mensaje)
    while comprobacion == False:
        print(f'> {mensaje}')
        mensaje = pedir_palabra()
        comprobacion = comprobar(mensaje)


if __name__ == '__main__':
    main()