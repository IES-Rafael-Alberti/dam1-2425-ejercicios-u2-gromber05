
def pregunta_tipo_pizza():
    n = input('¿Quieres la pizza vegetariana o no vegetariana?: ')
    return n.title()

def vegatariana_o_no(n: str) -> str:
    if n == 'Si':
        a = 'Vegetariana'
    else: 
        a = 'No vegetariana'
    return a

def ingredientes_vegetariana():
    print('La pizza posee mozzarella y tomate')
    print('Selecciona un ingrediente de los siguientes')
    
    n = input('Pimiento y Tofu\n')
    n = n.title()

    if n == 'Pimiento':
        return 'Pimiento'
    elif n == 'Tofu':
        return 'Tofu'

def ingredientes_no_vegetariana():
    print('La pizza posee mozzarella y tomate')
    print('Selecciona un ingrediente de los siguientes')

    n = input('Peperoni, Jamón y Salmón \n')
    n = n.title()

    if n == 'Peperoni':
        return 'Peperoni'
    elif n == 'Jamón':
        return 'Jamón'
    elif n == 'Salmón':
        return 'Salmón'

def main():
    n = pregunta_tipo_pizza()
    tipo = vegatariana_o_no(n)

    if tipo == 'Vegetariana':
        a = ingredientes_vegetariana()

    elif tipo == 'No vegetariana':
        a = ingredientes_no_vegetariana()

    print(f'El tipo de pizza que has pedido es {tipo} con los ingredientes Mozarella, Tomate y {a}')

if __name__ == "__main__":
    main()