

def quicksort(lista, bajo, alto):
    
    if bajo < alto:
        # pi es el índice de partición, lista[pi] está en la posición correcta
        pi = particion(lista, bajo, alto)
        
        # Ordenar los elementos por separado antes y después de la partición
        quicksort(lista, bajo, pi - 1)
        quicksort(lista, pi + 1, alto)

def particion(lista, bajo, alto):
    pivote = lista[bajo]  # Elegimos el primer elemento como pivote
    izquierda = bajo + 1
    derecha = alto

    while True:
        # Encuentra un elemento más grande que el pivote
        while izquierda <= derecha and lista[izquierda] <= pivote:
            izquierda += 1

        # Encuentra un elemento más pequeño que el pivote
        while izquierda <= derecha and lista[derecha] >= pivote:
            derecha -= 1

        # Si izquierda está a la derecha de derecha, intercambiamos los elementos
        if izquierda <= derecha:
            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]
        else:
            break

    # Intercambiar el pivote con el elemento en derecha
    lista[bajo], lista[derecha] = lista[derecha], lista[bajo]

    return derecha

# Prueba de la implementación
if __name__ == "__main__":
    lista_ejemplo = [10, 7, 8, 9, 1, 5]
    print("Lista original:", lista_ejemplo)
    quicksort(lista_ejemplo, 0, len(lista_ejemplo) - 1)
    print("Lista ordenada:", lista_ejemplo)
