
def pedir_monto():
    monto_total = 0
    monto = int(input('Introduzca el monto de la empresa: '))
    
    while monto != 0:
        if monto < 0:
            print('**ERROR** El monto ingresado no puede ser negativo')

        monto_total += monto
        monto = int(input('Introduzca el monto de la empresa: '))
        
    return monto_total

def calcular_descuento(monto):
    if monto > 1000:
        return True
    else:
        return False

def main():
    monto = pedir_monto()

    if calcular_descuento(monto) == True:
        descuento = monto * 0.10
        monto -= descuento

    print(f'El total a pagar sería de {monto}€')


if __name__ == '__main__':
    main()