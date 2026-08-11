def busca_binaria(lista, alvo):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2  
        chute = lista[meio]

        if chute == alvo:
            return meio  
        
        if chute > alvo:
            alto = meio - 1  
        else:
            baixo = meio + 1  

    return -1  
