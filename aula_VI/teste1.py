#O(1)
def pegar_primeiro_elemento(lista):
    # Não importa se a lista tem 10 ou 10 milhões de itens, 
    # o acesso direto por índice leva apenas 1 passo.
    return lista[0]

dados = [10, 20, 30, 40, 50]
print(pegar_primeiro_elemento(dados))  # Saída: 10



