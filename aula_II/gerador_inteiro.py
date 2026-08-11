import random

def list_random(qtd):
    lista = []

    for i in range(qtd):
        num = random.randint(0, 30)
        lista.append(num)

    return lista

resultado = list_random(30)

print(resultado)