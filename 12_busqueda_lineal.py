import random


def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break

    return match


if __name__ == "__main__":
    tamano_de_lista = int(input("De que tamano sera la lista? "))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)

    objetivo = int(input("Que numero quieres encontrar? "))

    encontrado = busqueda_lineal(lista, objetivo)
    print(
        f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
