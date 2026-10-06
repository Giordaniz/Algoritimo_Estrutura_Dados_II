from gerador_nums_inteiros import lista_de_inteiros
from lista import Lista
from nodo import Nodo


def adicionar_numeros_na_lista(minha_lista):
    for num in lista_de_inteiros:
        minha_lista.adicionar(Nodo(num))

def selection_sort(lista):
    if not lista:
        return lista
    for i in range(len(lista)):
        min_i = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_i]:
                min_i = j
        lista[i], lista[min_i] = lista[min_i], lista[i]

    print(lista)


selection_sort([2, 4, 3, 6, 9, 1, 6, 3])

lista_ED = Lista()
adicionar_numeros_na_lista(lista_ED)
lista_ED.print()
# print("ok")
# elemento_localizar = int(input("Localizar o elemento: "))
# input(f"Vou localizar o elemento {elemento_localizar}")
# print(lista_ED.index(elemento_localizar))

lista_ED.ordena_bubble()
lista_ED.print()
