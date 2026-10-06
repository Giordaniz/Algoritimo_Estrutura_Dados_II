import string

class No:
    """Classe que representa um nó da Árvore Binária de Busca."""
    def __init__(self, palavra):
        self.palavra = palavra
        self.contador = 1
        self.esquerdo = None
        self.direito = None


class ArvoreBinariaBusca:
    """Implementação da Árvore Binária de Busca (ABB) para contagem de palavras."""
    def __init__(self):
        self.raiz = None
        self.total_palavras_lidas = 0

    def _limpar_palavra(self, palavra):
        """Converte para minúsculo e remove pontuações."""
        palavra = palavra.lower()
        # Remove caracteres de pontuação
        return palavra.strip(string.punctuation)

    def inserir(self, palavra_bruta):
        """Processa e insere uma palavra na árvore."""
        palavra = self._limpar_palavra(palavra_bruta)
        if not palavra:
            return  # Ignora strings vazias geradas por remoção de pontuação

        self.total_palavras_lidas += 1
        if self.raiz is None:
            self.raiz = No(palavra)
        else:
            self._inserir_recursivo(self.raiz, palavra)

    def _inserir_recursivo(self, no_atual, palavra):
        if palavra == no_atual.palavra:
            no_atual.contador += 1
        elif palavra < no_atual.palavra:
            if no_atual.esquerdo is None:
                no_atual.esquerdo = No(palavra)
            else:
                self._inserir_recursivo(no_atual.esquerdo, palavra)
        else:
            if no_atual.direito is None:
                no_atual.direito = No(palavra)
            else:
                self._inserir_recursivo(no_atual.direito, palavra)

    def buscar(self, palavra_bruta):
        """Busca uma palavra na árvore e retorna o nó ou None."""
        palavra = self._limpar_palavra(palavra_bruta)
        return self._buscar_recursivo(self.raiz, palavra)

    def _buscar_recursivo(self, no_atual, palavra):
        if no_atual is None or no_atual.palavra == palavra:
            return no_atual
        if palavra < no_atual.palavra:
            return self._buscar_recursivo(no_atual.esquerdo, palavra)
        return self._buscar_recursivo(no_atual.direito, palavra)

    def processar_texto(self, texto):
        """Lê uma string completa e insere palavra por palavra."""
        # Divide o texto por espaços em branco
        palavras = texto.split()
        for p in palavras:
            self.inserir(p)

    def processar_arquivo(self, caminho_arquivo):
        """Lê um arquivo de texto e insere palavra por palavra."""
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                for linha in f:
                    palavras = linha.split()
                    for p in palavras:
                        self.inserir(p)
            return True
        except FileNotFoundError:
            print("Erro: Arquivo não encontrado.")
            return False
        except Exception as e:
            print(f"Erro ao ler arquivo: {e}")
            return False

    # ---------------------------------------------------------
    # Listagem Em-Ordem (In-Order)
    # ---------------------------------------------------------
    def exibir_em_ordem(self):
        """Listagem em ordem alfabética de todas as palavras."""
        if self.raiz is None:
            print("Árvore vazia.")
            return
        self._em_ordem_recursivo(self.raiz)

    def _em_ordem_recursivo(self, no_atual):
        if no_atual:
            self._em_ordem_recursivo(no_atual.esquerdo)
            print(f"- {no_atual.palavra}: {no_atual.contador} ocorrência(s)")
            self._em_ordem_recursivo(no_atual.direito)

    # ---------------------------------------------------------
    # Informações e Estatísticas da Árvore
    # ---------------------------------------------------------
    def _obter_todos_nos(self, no_atual, lista_nos):
        """Auxiliar em-ordem para coletar referências aos nós."""
        if no_atual:
            self._obter_todos_nos(no_atual.esquerdo, lista_nos)
            lista_nos.append(no_atual)
            self._obter_todos_nos(no_atual.direito, lista_nos)

    def contar_nos(self, no_atual):
        """Retorna a quantidade de nós únicos (palavras distintas)."""
        if no_atual is None:
            return 0
        return 1 + self.contar_nos(no_atual.esquerdo) + self.contar_nos(no_atual.direito)

    def calcular_altura(self, no_atual):
        """Retorna a altura da árvore."""
        if no_atual is None:
            return -1  # Altura da árvore vazia é -1 (ou 0 para nó folha isolado)
        altura_esq = self.calcular_altura(no_atual.esquerdo)
        altura_dir = self.calcular_altura(no_atual.direito)
        return 1 + max(altura_esq, altura_dir)

    def contar_folhas(self, no_atual):
        """Retorna a quantidade de nós folha."""
        if no_atual is None:
            return 0
        if no_atual.esquerdo is None and no_atual.direito is None:
            return 1
        return self.contar_folhas(no_atual.esquerdo) + self.contar_folhas(no_atual.direito)

    def palavra_mais_frequente(self):
        """Retorna o nó com a maior ocorrência."""
        todos_nos = []
        self._obter_todos_nos(self.raiz, todos_nos)
        if not todos_nos:
            return None
        
        mais_frequente = todos_nos[0]
        for no in todos_nos:
            if no.contador > mais_frequente.contador:
                mais_frequente = no
        return mais_frequente

    # ---------------------------------------------------------
    # Desafio: Top 10 Palavras Mais Frequentes
    # ---------------------------------------------------------
    def exibir_top_10(self):
        """Exibe as 10 palavras mais frequentes sem usar dicts/maps."""
        todos_nos = []
        self._obter_todos_nos(self.raiz, todos_nos)
        
        if not todos_nos:
            print("Nenhuma palavra cadastrada.")
            return

        # Ordena a lista de nós decrescente pela contagem de ocorrências
        # Utilizando a função embutida sort com chave lambda (sem utilizar dicionários)
        todos_nos.sort(key=lambda no: no.contador, reverse=True)

        top_10 = todos_nos[:10]
        print("\n--- TOP 10 PALAVRAS MAIS FREQUENTES ---")
        for i, no in enumerate(top_10, start=1):
            print(f"{i}º: '{no.palavra}' -> {no.contador} ocorrência(s)")


# ---------------------------------------------------------
# Menu do Sistema
# ---------------------------------------------------------
class SistemaArvore:
    def __init__(self):
        self.arvore = ArvoreBinariaBusca()

    def menu(self):
        while True:
            print("\n===== MENU =====")
            print("1 - Digitar texto")
            print("2 - Ler arquivo")
            print("3 - Buscar palavra")
            print("4 - Exibir índice (Ordem Alfabética)")
            print("5 - Mostrar estatísticas")
            print("6 - Mostrar informações da árvore")
            print("7 - Exibir Top 10 mais frequentes (Desafio)")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                texto = input("\nDigite o texto desejado:\n")
                self.arvore.processar_texto(texto)
                print("Texto processado com sucesso!")

            elif opcao == "2":
                caminho = input("\nDigite o caminho/nome do arquivo (.txt): ").strip()
                if self.arvore.processar_arquivo(caminho):
                    print("Arquivo lido e processado com sucesso!")

            elif opcao == "3":
                palavra = input("\nDigite a palavra que deseja buscar: ").strip()
                no_encontrado = self.arvore.buscar(palavra)
                if no_encontrado:
                    print(f"\n[SUCESSO] A palavra '{no_encontrado.palavra}' foi encontrada!")
                    print(f"Ocorrências: {no_encontrado.contador}")
                else:
                    print(f"\n[NÃO ENCONTRADO] A palavra '{palavra}' não foi cadastrada na árvore.")

            elif opcao == "4":
                print("\n=== ÍNDICE DE PALAVRAS (ORDEM ALFABÉTICA) ===")
                self.arvore.exibir_em_ordem()

            elif opcao == "5":
                print("\n=== ESTATÍSTICAS DO TEXTO ===")
                total_lidas = self.arvore.total_palavras_lidas
                palavras_distintas = self.arvore.contar_nos(self.arvore.raiz)
                mais_freq = self.arvore.palavra_mais_frequente()

                print(f"Total de palavras lidas: {total_lidas}")
                print(f"Total de palavras distintas: {palavras_distintas}")
                if mais_freq:
                    print(f"Palavra mais frequente: '{mais_freq.palavra}' ({mais_freq.contador} ocorrências)")
                else:
                    print("Nenhuma palavra registrada.")

            elif opcao == "6":
                print("\n=== INFORMAÇÕES DA ÁRVORE ===")
                raiz = self.arvore.raiz
                print(f"Altura da árvore: {self.arvore.calcular_altura(raiz)}")
                print(f"Quantidade de nós: {self.arvore.contar_nos(raiz)}")
                print(f"Quantidade de folhas: {self.arvore.contar_folhas(raiz)}")

            elif opcao == "7":
                self.arvore.exibir_top_10()

            elif opcao == "0":
                print("Encerrando o programa...")
                break
            else:
                print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    app = SistemaArvore()
    app.menu()