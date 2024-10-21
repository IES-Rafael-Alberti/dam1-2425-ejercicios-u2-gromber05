
from libreria import pedirnumero

def par_o_impar(num: int):
    num = num % 2
    return num

def main():
    num = pedirnumero()
    
    if par_o_impar(num) == 0:
        print('Es par')
    else: 
        print('Es impar')


if __name__ == "__main__":
    main()