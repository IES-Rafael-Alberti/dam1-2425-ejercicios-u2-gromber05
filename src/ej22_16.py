from libreria import pedir_numero
    
def comprobar_mayor(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def comprobar_cero(num):
    if num == 0:
        return True
    else:
        return False
    
def main():
    num = pedir_numero()
    mayor = num

    while comprobar_cero(num) == False:
        if comprobar_mayor(num, mayor) == num:
            mayor = num
        num = pedir_numero()

    print(f'El mayor número ingresado fue {mayor}')

if __name__ == '__main__':
    main()