import os

def borrar_cache():
    os.system("cls")

def pedir_numero():
    try:
        n = int(input('Introduzca un número: '))
        if n > 20:
            raise ValueError('**ERROR** El número solo puede ser menor que veinte')
        if n < 0:
            raise ValueError('**ERROR** El número solo puede ser mayor a cero')
    
    except ValueError:
        print('**ERROR** Solo puedes introducir un número')
        n = pedir_numero()
        
    
    return n

def piramide(num: int):
    serie = ''
    total = 0
    for i in range(num + 1):
        total += i 
    for i in reversed(range(num + 1)):
        
        if i == 0:
            i = str(i)
            serie += i + ' = '
        else:
            i = str(i)
            serie += i + ' + '
    return serie, str(total)

def piramide_inversa(num: int):
    serie = ''
    total = 0
    for i in range(num + 1):
        total += i 
    for i in range(num + 1):
        
        if i == num:
            i = str(i)
            serie += i + ' = '
        else:
            i = str(i)
            serie += i + ' + '
    return serie, str(total)
    
def main():
    borrar_cache()
    num = pedir_numero()
    print('Su piramide de sumas es la siguiente: \n')
    for i in reversed(range(num + 1)):
        serie, total = piramide_inversa(i)
        print(f'{i} => {serie}{total}')
    for i in range(1, num + 1):
        serie, total = piramide(i)
        print(f'{i} => {serie}{total}')

    comprobacion = input('\n¿Quiere hacer otra piramide (S/N)? \n').lower()
    
    if comprobacion == 's':
        borrar_cache()
        main()
    else:
        print('Hasta luego')

if __name__ == "__main__":
    main()