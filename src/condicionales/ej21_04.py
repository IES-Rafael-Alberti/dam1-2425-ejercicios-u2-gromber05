
from libreria import pedir_numero

def par_o_impar(num: int):
    return num % 2

def main():
    num = pedir_numero()
    
    if par_o_impar(num) == 0:
        print('Es par')
    else: 
        print('Es impar')


if __name__ == "__main__":
    main()