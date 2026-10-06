class lista:
    def __init__(self):
        self.cabeca = None
        self.trail = None

    def ordena_selection(self):
        atual = self.head
        while atual is not None:
            menor = atual.back
            proximo = atual.back
            while proximo is not None:
                if proximo.valor < menor.valor:
                    menor = proximo
                proximo = proximo.back
            if menor != atual:
                atual.valor, menor.valor = menor.valor, atual.valor
            atual = atual.back
        