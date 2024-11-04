
def pedir_contraseña():
    return input('Introduzca su contraseña: ')

def comprobar_contraseña(contra):
    try:
        if contra != 'contraseña':
            raise NameError('Incorrect Password!!')
        else:
            print('La contraseña es correcta')

    except NameError as e:
        print(e)

def main():
    contra = pedir_contraseña()
    comprobar_contraseña(contra)

if __name__ == '__main__':
    main()