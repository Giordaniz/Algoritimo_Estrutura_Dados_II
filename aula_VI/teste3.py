
#O(n)
def procurar_item_linear(lista, item_procurado):
    # No pior cenário, o item está no final da lista ou não existe.
    # O loop precisará rodar 'n' vezes (tamanho total da lista).
    for item in lista:
        if item == item_procurado:
            return True
    return False

nomes = ["Ana", "Bruno", "Carlos", "Diana"]
print(procurar_item_linear(nomes, "Diana"))  # Saída: True
