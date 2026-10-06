from insertion_sort_listas import insertion_sort
from gerador_nums_inteiros import lista_inteiros
from nodo import nodo

def adicionar_numeros_na_lista(lista):
        for num in insertion_sort(lista):
            lista.adicionar(nodo(num))

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

lista_ED = lista_inteiros()
adicionar_numeros_na_lista(lista_ED)
lista_ED.print()
lista_ED.ordena_bubble()
lista_ED.print()

