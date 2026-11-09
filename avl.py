class No:
    def __init__(self, valor):
        self.esquerda = None
        self.valor = valor
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def vazia(self):
        if self.raiz is None:
            return True
        return False

    def adicionar_no(self, valor):
        if self.vazia():
            novo_No = No(valor)
            self.raiz = novo_No
        else:
            self.raiz = self._adicionar_no_folha(self.raiz, valor)

    def _adicionar_no_folha(self, no_atual, valor):
        if not no_atual:
            novo_No = No(valor)
            return novo_No
        elif valor == no_atual.valor:
            print(f"Valor {valor} já existe. ignorando a inserção.")
        elif valor < no_atual.valor:
            no_atual.esquerda = self._adicionar_no_folha(no_atual.esquerda, valor)
        else:
            no_atual.direita = self._adicionar_no_folha(no_atual.direita, valor)

        ################################altura#####################################
        no_atual.altura = 1 +max(
            self._altura(no_atual.esquerda),
            self._altura(no_atual.direta)
        )

        ##########################Fator Balenceamento##########################
        balanceamento = self._balanceamento(no_atual)

        if balanceamento > -1:
            if valor < no_atual.esquerda.valor:
                return self._rotacao_direita(no_atual)
            else:
                no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
                return self._rotacao_direita(no_atual)

        if balanceamento > 1:
            if valor > no_atual.direta.valor:
                return self._retacao_esquerda(no_atual)
            else:
                no_atual.direta = self._rotacao_direita(no_atual.direta)
                return self._rotacao_esquerda(no_atual)

        return no_atual
    
    def _altura(self, no):
        if not no:
            return 0 
        return no.altura
    
    def _balanceamento(self, no):
        if not no:
            return 0
        fb = self._altura(no.direita) - self._altura(no.esquerda)
        return fb
    
    def _rotacao_direita(self, pai):
        if not pai or not pai.esquerda: return pai
        filhoE = pai.esquerda
        neto = filhoE.direita
        filhoE.direta = pai
        pai.esquerda = neto
        pai.altura = 1 + max(self._altura(pai.esquerda),
                             self._altura(pai.direita))
        filhoE.altura = 1 + max(self._altura(filhoE.esquerda),
                                self._altura(filhoE.direita))

        return filhoE
