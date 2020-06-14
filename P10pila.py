def insertar(lista, dato):
    lista.append(dato)
    

def borrar(lista):
    dato = lista.pop()
    return dato 

def imprimi_pila(lista):
    lista.reverse()
    for x in lista:
        print(x)
    print()
    lista.reverse()
        

def main():
    pila = [0]
    insertar(pila, "lista1")
    insertar(pila, 2)
    imprimi_pila(pila)
    print()
    print(borrar(pila))
    imprimi_pila(pila)


if __name__ == "__main__":
    main()
