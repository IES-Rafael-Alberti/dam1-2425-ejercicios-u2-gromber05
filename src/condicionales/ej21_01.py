from libreria import preguntar_edad

def comprobarEdad(edad) -> int:
    if edad >= 18:
        return True
    else:
        return False
    
def main():
    edad = preguntar_edad()
    comprobacion = comprobarEdad(edad)

    if comprobacion == True:
        print(f'Tienes {edad} por tanto, eres mayor de edad')
    else:
        print(f'Tienes {edad} por tanto, no eres mayor de edad')

if __name__ == "__main__":
    main()