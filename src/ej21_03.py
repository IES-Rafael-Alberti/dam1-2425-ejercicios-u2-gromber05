# ZeroDivisionError
from libreria import pedir_numero
    
def division(num:int , num2:int) -> float:
    return num/num2

def comprobar_cero(num: int) -> bool:
    return num != 0
    
def main():
    num = pedir_numero()
    num2 = pedir_numero()

    if (num is not None) and (num2 is not None):
        if not comprobar_cero(num2):
            print('El segundo número no puede ser 0')
        else:
            div = division(num, num2)
            print(f'La división entre {num} y {num2} tiene como resultado {div}')
    else:
        print('¡Solo puedes introducir números!')


if __name__ == "__main__":
    main()