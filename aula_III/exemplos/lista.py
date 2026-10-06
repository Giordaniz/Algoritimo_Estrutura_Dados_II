class Lista:
    def __init__(self):
        self.elemento = None
        self.fim = None

    def vazio(self):
        if self.elemento is None:
            return True
        return False

    def adicionar(self, novo_elemento):
        if self.vazio():
            self.elemento = novo_elemento
            self.fim      = novo_elemento
            return
        
        self.fim.proximo = novo_elemento
        self.fim         = novo_elemento

    def print(self):
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        elemento = self.elemento
        while elemento:
            print(
                f"End.Atual: {str(elemento)[-5:]} - {elemento.valor} - {str(elemento.proximo)[-5:]}")
            elemento = elemento.proximo

    def index(self, valor):
        elemento = self.elemento
        while elemento:
            if elemento.valor == valor:
                return f"--- Valor {valor} encontrado no elemento {str(elemento)[-5:]}"
            elemento = elemento.proximo
        return f"---- Valor {valor} não encontrado em nenhum elemento da lista! "

    def ordena_bubble(self):
        if self.elemento is None or self.elemento.proximo is None:
            return

        fim = None

        while fim != self.elemento:
            atual = self.elemento
            trocou = False

            while atual.proximo != fim:
                proximo = atual.proximo
                if atual.valor > proximo.valor:
                    atual.valor, proximo.valor = proximo.valor, atual.valor
                    trocou = True
                atual = atual.proximo

            fim = atual

            if not trocou:
                break

