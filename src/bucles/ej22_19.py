import os
import time

def borrar_cache():
    os.system("cls")

def seleccion():
    sel = int(input('\nElige una opción:\n 1.- Comenzar programa\n 2.- Imprimir listado\n 3.- Finalizar programa\n\n>'))
    return sel

def menu():
    sel = seleccion()
    quitar_programa = False

    while quitar_programa == False:
        while sel > 3 or sel < 1:
            print('**ERROR** La selección no está reconocida')
            sel = int(input())
        else:
            if sel == 1:
                print('Has realizado la selección uno')
                sel = seleccion()
            elif sel == 2:
                print('Has realizado la selección dos')
                sel = seleccion()
            elif sel == 3:
                print('\n\nHasta luego ')
                time.sleep(2)
                borrar_cache()
                break
    
            

def main():
    menu()

if __name__ == '__main__':
    main()