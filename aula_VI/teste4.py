def encontrar_duplicatas_visual(lista):
    n = len(lista)
    total_operacoes = 0
    
    print(f"Analisando lista de tamanho n = {n}: {lista}")
    print("-" * 55)
    
    # Loop Externo: Escolhe o primeiro item da comparação
    for i in range(n):
        print(f"Loop Externo -> Fixou o item da posição {i}: '{lista[i]}'")
        
        # Loop Interno: Compara o item escolhido com todos os outros
        for j in range(n):
            total_operacoes += 1
            
            # Não compara o item com ele mesmo na mesma posição
            if i != j and lista[i] == lista[j]:
                print(f"   [!] OPERAÇÃO {total_operacoes}: Comparando '{lista[i]}' com '{lista[j]}' -> DUPLICATA ENCONTRADA!")
            else:
                print(f"   [.] OPERAÇÃO {total_operacoes}: Comparando '{lista[i]}' com '{lista[j]}'")
                
        print("-" * 55)
        
    print(f"--> Fim do Algoritmo! Para n={n} elementos, foram feitas {total_operacoes} operações.")

# Executando o exemplo com uma lista pequena de 4 elementos
dados = ["A", "B", "C", "A"]
encontrar_duplicatas_visual(dados)
