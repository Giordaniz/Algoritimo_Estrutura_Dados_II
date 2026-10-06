#O(Logn)
def busca_binaria(lista_ordenada, item):
    baixo = 0
    alto = len(lista_ordenada) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista_ordenada[meio]
        if chute == item:
            return meio  # Retorna o índice do item encontrado
        if chute > item:
            alto = meio - 1  # O item está na metade esquerda
        else:
            baixo = meio + 1  # O item está na metade direita
    return None
numeros = [1, 3, 5, 7, 9, 11, 13, 15]
print(busca_binaria(numeros, 7))  # Saída: 3 (índice do número 7)
