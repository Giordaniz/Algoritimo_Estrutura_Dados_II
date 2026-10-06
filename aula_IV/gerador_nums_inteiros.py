import random


def lista_inteiros(tamanho_lista:int = 10, intervalo_maximo:int = 10) -> list:
    # lista = [random.randint(0, intervalo_maximo) for _ in range(tamanho_lista)]
    lista = random.sample(range(0, intervalo_maximo), tamanho_lista)

    return lista

lista_de_inteiros = lista_inteiros() #random.sample(range(0, 100), 50)



