
from libreria import pedirnumero

def pedir_edad():
    num = None
    while num == None:
        num = int(input("Introduce tu edad: "))
    return num

def pedir_ingresos():
    num = None
    while num == None:
        num = int(input("Introduce tus ingresos: "))
    return num


def comprobar_edad(num: int) -> bool:
    if num > 16:
        return True
    else: 
        return False
    
def comprobar_ingresos(num: int) -> bool:
    if num >= 1000:
        return True
    else:
        return False

def main():
    edad = pedir_edad()
    ingresos = pedir_ingresos()

    if comprobar_edad(edad) == True:
        if comprobar_ingresos(ingresos) == True:
            print('Debes tributar')
        else:
            print('No debes tributar')
    else:
        print('No debes tributar')

if __name__ == "__main__":
    main()