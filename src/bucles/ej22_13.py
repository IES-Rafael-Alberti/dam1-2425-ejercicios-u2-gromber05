import os

def pedir_palabra():
    mensaje = input('')
    return mensaje

def comprobar(mensaje: str):
    return mensaje.lower() == 'salir'

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