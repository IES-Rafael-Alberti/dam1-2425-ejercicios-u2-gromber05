
def pedir_numero():
    try:
        num = int(input('Introduzca un número: '))

    except ValueError:
        num = f'\n**ERROR**\n El valor introducido solo puede ser un número\n **ERROR**\n'
    except:
        num = f'\n**ERROR**\n Error desconocido \n**ERROR**\n'
    return num

def separar_numero(num):
    numeros = list(str(num))
    return numeros

def calcular_par_impar(num):
    num = int(num)
    n = num % 2
    return n == 0

def descomponer(num):
    return list(str(num))

def main():
    contador_par = 0
    contador_impar = 0
    lista_par =  []
    lista_impar = []

    num = pedir_numero()
    while num != 0:
        
        digitos = descomponer(num)
        for i in digitos:
            i = int(i)
            situar = calcular_par_impar(i)
            
            if situar == True:
                contador_par += 1
                lista_par.append(i)
            else: 
                contador_impar += 1
                lista_impar.append(i)

        num = pedir_numero()

    print("Dígitos pares:", lista_par)
    print("Dígitos impares:", lista_impar)
    print("Total de dígitos pares:", contador_par)
    print("Total de dígitos impares:", contador_impar)

if __name__ == '__main__':
    main()