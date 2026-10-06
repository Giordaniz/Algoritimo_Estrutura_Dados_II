class No:
    def __init__(self, valor):
        self.valor = valor
        self.filhos = []

    def adicionar_filho(self, filho):
        self.filhos.append(filho)


class Arvore:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def vazia(self):
        return self.raiz is None

    def adicionar_no(self, valor, pai=None):
        novo_no = No(valor)

        if pai is None:
            if self.raiz is None:
                self.raiz = novo_no
            else:
                raise ValueError("A árvore já possui raiz.")
        else:
            no_encontrado = self.buscar_no(pai)
            if no_encontrado:
                no_encontrado.adicionar_filho(novo_no)
            else:
                raise ValueError(f"Nó pai '{pai}' não encontrado.")

    def buscar_no(self, valor, no=None):
            if no is None:
                no = self.raiz
            if no is None:
                return None
    
            if no.valor == valor:
                return no
    
            for filho in no.filhos:
                resultado = self.buscar_no(valor, filho)
                if resultado:
                    return resultado
            return None
    
    def imprimir(self, no=None, nivel=0):
            if self.vazia():
                print("------ Árvore vazia ------")
                return
    
            if no is None:
                no = self.raiz
    
            print(" " * (nivel * 2) + f"- {no.valor}")
            for filho in no.filhos:
                self.imprimir(filho, nivel + 1)

def adicionar_ramo(arvore):
    while True:
        arvore.imprimir()
        print("\nEntre com os dados ou ENTER para encerrar!")
        valor = input("Digite o valor/dado a ser inserido: ")
        if not valor:
            break
        ramo = None
        if not arvore.vazia():
            ramo  = input("Digite o pai para esse dado: ")
            if not ramo:
                break
        arvore.adicionar_no(valor, ramo)


arvore = Arvore()
adicionar_ramo(arvore)

