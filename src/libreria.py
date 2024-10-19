
def pedirnumero2():
    num = None
    while num == None:
        num = int(input("Introduce un número: "))
    return num


def pedirnumero():
    num = None
    try:
        num = int(input("Introduce un número: "))
    except ValueError:
        print('')