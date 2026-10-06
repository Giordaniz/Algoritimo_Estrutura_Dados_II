class No:
    def __init__(self, palavra):
        self.palavra = palavra
        self.contador = 1
        self.esquerda = None
        self.direita = None

    def adicionar_filho(self, filho):
        self.filhos.append(filho)


class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None
        self.total_palavras_lidas = 0

    def limpar_palavra(self, palavra):
        palavra = palavra.lower()
        palavra = ''.join(caractere for caractere in palavra if caractere not in string.punctuation)
        return palavra

    def processar_textos(self, texto):
        palavras = texto.split()
        for p in palavras:
            if p_limpa in palavras:
              p_limpa = self.limper_palavra(p) if hasattr(self, 'limper_palavra') else self.limpar_palavra(p)
            if p_limpa: 
                self.total_palavras_lidas += 1
                self.inserir(p_limpa)  

    def inserir(self, palavra):
        if self.raiz is None:
            self.raiz = No(palavra)
        else:
            self._inserir_recursivo(self.raiz, palavra)


    def _inserir_recursivo(self, no_atual, palavra):
        if palavra < no_atual.palavra:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(palavra)
            else:
                self._inserir_recursivo(no_atual.esquerda, palavra)
        else:
            if no_atual.direita is None:
                no_atual.direita = No(palavra)
            else:
                self._inserir_recursivo(no_atual.direita, palavra)

    def buscar(self, palavra):
        p_limpa = self.limpar_palavra(palavra)
        return self._buscar_recursivo(self.raiz, p_limpa)

    def _buscar_recursivo(self, no_atual, palavra):
        if no_atual is None or no_atual.palavra == palavra:
            return no_atual
        if palavra < no_atual.palavra:
            return self._buscar_recursivo(no_atual.esquerda, palavra)
        return self._buscar_recursivo(no_atual.direita, palavra)

    def exibir_em_ordem(self):
        if self.raiz is None:
            print("A árvore está vazia.")
        else:
            self._exibir_em_ordem_recursivo(self.raiz)

    def _exibir_em_ordem_recursivo(self, no_atual):
        if no_atual is not None:
            self._exibir_em_ordem_recursivo(no_atual.esquerda)
            print(f"{no_atual.palavra}: {no_atual.contador}x")
            self._exibir_em_ordem_recursivo(no_atual.direita)

    def obter_altura(self, no_atual):
        if no_atual is None:
            return -1  
        altura_esq = self.obter_altura(no_atual.esquerda)
        altura_dir = self.obter_altura(no_atual.direita)
        return 1 + max(altura_esq, altura_dir)

    def contar_nos(self, no_atual):
        if no_atual is None:
            return 0
        return 1 + self.contar_nos(no_atual.esquerda) + self.contar_nos(no_atual.direita)

    def contar_folhas(self, no_atual):
        if no_atual is None:
            return 0
        if no_atual.esquerda is None and no_atual.direita is None:
            return 1
        return self.contar_folhas(no_atual.esquerda) + self.contar_folhas(no_atual.direita)

    def obter_altura(self, no_atual):
        if no_atual is None:
            return -1  
        altura_esq = self.obter_altura(no_atual.esquerda)
        altura_dir = self.obter_altura(no_atual.direita)
        return 1 + max(altura_esq, altura_dir)

    def contar_nos(self, no_atual):
        if no_atual is None:
            return 0
        return 1 + self.contar_nos(no_atual.esquerda) + self.contar_nos(no_atual.direita)

    def contar_folhas(self, no_atual):
        if no_atual is None:
            return 0
        if no_atual.esquerda is None and no_atual.direita is None:
            return 1
        return self.contar_folhas(no_atual.esquerda) + self.contar_folhas(no_atual.direita)
  
    def _achatá_arvore(self, no_atual, lista_elementos):
    
        if no_atual is not None:
            self._achatá_arvore(no_atual.esquerda, lista_elementos)
            lista_elementos.append(no_atual)
            self._achatá_arvore(no_atual.direita, lista_elementos)

    def exibir_estatisticas(self):
        if self.raiz is None:
            print("Nenhum dado processado ainda.")
            return

        lista_elementos = []
        self._achatá_arvore(self.raiz, lista_elementos)

        mais_frequente = lista_elementos[0]
        for no in lista_elementos:
            if no.contador > mais_frequente.contador:
                mais_frequente = no

        print(f"\n--- Estatísticas do Texto ---")
        print(f"Total de palavras lidas: {self.total_palavras_lidas}")
        print(f"Total de palavras distintas (Nós): {len(lista_elementos)}")
        print(f"Palavra mais frequente: '{mais_frequente.palavra}' ({mais_frequente.contador} ocorrências)")

    def exibir_top_10(self):
        if self.raiz is None:
            print("A árvore está vazia.")
            return

        lista_elementos = []
        self._achatá_arvore(self.raiz, lista_elementos)
        lista_elementos.sort(key=lambda no: no.contador, reverse=True)

        print("\n--- TOP 10 PALAVRAS MAIS FREQUENTES ---")
        for i, no in enumerate(lista_elementos[:10], start=1):
            print(f"{i}º - '{no.palavra}' com {no.contador} ocorrências")

def menu(self):
        while True:
            print("\n===== MENU =====")
            print("1 - Digitar texto")
            print("2 - Ler arquivo")
            print("3 - Buscar palavra")
            print("4 - Exibir índice")
            print("5 - Mostrar estatísticas")
            print("6 - Mostrar informações da árvore")
            print("7 - Desafio: Mostrar TOP 10 frequentes")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                texto = input("\nDigite ou cole o seu texto aqui:\n")
                self.processar_texto(texto)
                print("Texto processado e inserido na árvore com sucesso!")

            elif opcao == "2":
                caminho = input("\nDigite o caminho ou nome do arquivo (.txt): ")
                if os.path.exists(caminho):
                    with open(caminho, 'r', encoding='utf-8') as arquivo:
                        texto = arquivo.read()
                    self.processar_texto(texto)
                    print("Arquivo lido e inserido na árvore com sucesso!")
                else:
                    print("Arquivo não encontrado. Verifique o nome e tente novamente.")

            elif opcao == "3":
                palavra = input("\nDigite a palavra que deseja buscar: ")
                resultado = self.buscar(palavra)
                if resultado:
                    print(f"Encontrada! A palavra '{resultado.palavra}' aparece {resultado.contador} vez(es) no texto.")
                else:
                    print(f"A palavra '{palavra}' não foi encontrada na árvore.")

            elif opcao == "4":
                print("\n--- Índice em Ordem Alfabética ---")
                self.exibir_em_ordem()

            elif opcao == "5":
                self.exibir_estatisticas()

            elif opcao == "6":
                print(f"\n--- Informações da Árvore ---")
                print(f"Altura da árvore: {self.obter_altura(self.raiz)}")
                print(f"Quantidade total de nós: {self.contar_nos(self.raiz)}")
                print(f"Quantidade de folhas: {self.contar_folhas(self.raiz)}")

            elif opcao == "7":
                self.exibir_top_10()

            elif opcao == "0":
                print("Encerrando o programa. Até logo!")
                break
            else:
                print("Opção inválida! Tente novamente.")


        if __name__ == "__main__":
            app = ArvoreBinariaBusca()
            app.menu()

arvore = ArvoreBinariaBusca()

