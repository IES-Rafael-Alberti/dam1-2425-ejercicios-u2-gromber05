"""
Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.
"""
import os
from libreria import pedir_numero

def calcular_primo(num):
    divisores_num = 0

    for i in range(1, num):
        divisores = num % i
        if divisores == 0:
            divisores_num += 1
    return divisores_num

def detectar_negativo(num):
    if num < 0:
        raise ValueError('El número introducido no puede ser negativo')

def borrar_cache():
    os.system('cls')

def main():
    borrar_cache()
    contador_primos = 0

    num = pedir_numero()
    detectar_negativo(num)
    while num != 0:
        primos = calcular_primo(num)
        if primos <= 1:
            contador_primos += 1
        num = pedir_numero()
        detectar_negativo(num)    
    
    print(f'Se han ingresado {contador_primos} números primos')

if __name__ == '__main__':
    main()
    
