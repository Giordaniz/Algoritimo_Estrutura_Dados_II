import random
import gerador_inteiro as li 

def busca(lista_entrada:list, elemento_loc:int) -> int:
    for indice, elemento in enumerate(lista_entrada):
        if elemento == elemento_loc:
            return indice
    return None

print("gerar lista:")
lista_n_ordenada = li.gerar_lista_inteiros(10,15)

