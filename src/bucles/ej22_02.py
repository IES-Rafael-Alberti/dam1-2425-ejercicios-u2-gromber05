from libreria import preguntar_edad

def bucle(edad: int):
    for i in range(1,edad+1):
        print(i)

def main():
    edad = preguntar_edad()
    bucle(edad)

if __name__ == '__main__':
    main()