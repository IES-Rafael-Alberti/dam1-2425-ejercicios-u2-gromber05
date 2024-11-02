
def pedir_inversion():
    num = None
    while num == None:
        num = int(input('Introduzca su cantidad a invertir: '))
    return num

def pedir_interes_anual():
    num = None
    while num == None:
        num = int(input('Introduzca su interés anual: '))
    return num

def pedir_anios():
    num = None
    while num == None:
        num = int(input('Introduzca cuantos años va a invertir: '))
    return num

def calcular_intereses(cantidad: float, interes: float):

    cantidad *= interes / 100
    return cantidad
    

def main():
    cantidad = pedir_inversion()
    interes = pedir_interes_anual()
    anios = pedir_anios()

    total = 0
    for i in range(0, anios):
        t1 = calcular_intereses(cantidad, interes)
        total += t1
        print(total)


if __name__ == '__main__':
    main()