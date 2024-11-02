
def pedir_contraseña() -> str:
    return input("Introduzca una contraseña: ")

def comprobar(contraseña: str, contraseña_usuario: str):
    if contraseña.title() == contraseña_usuario.title():
        print("¡Ambas contraseñas coinciden!")
    else:
        print('Las contraseñas no coinciden')
        main()

def main():
    contraseña = 'contraseña'
    contraseña_usuario = pedir_contraseña()
    comprobar(contraseña, contraseña_usuario)

if __name__ == "__main__":
    main()