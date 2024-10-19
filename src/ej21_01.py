def comprobarEdad(edad) -> int:
    if edad >= 18:
        return True
    else:
        return False
    
def pedirEdad() -> int:
    edad = int(input('Introduzca su edad: '))
    return edad

def main():
    edad = pedirEdad()
    comprobacion = comprobarEdad(edad)

    if comprobacion == True:
        print(f'Tienes {edad} por tanto, eres mayor de edad')
    else:
        print(f'Tienes {edad} por tanto, no eres mayor de edad')

if __name__ == "__main__":
    main()