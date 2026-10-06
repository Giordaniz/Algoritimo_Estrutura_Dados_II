
class No:
    def __init__(self, nome, tipo, tamanho=None, pai=None):
        self.nome = nome
        self.tipo = tipo       
        self.tamanho = tamanho 
        self.filhos = []       
        self.pai = pai         

    def adicionar_filho(self, filho):
        filho.pai = self
        self.filhos.append(filho)

class ArvoreArquivos:
    def __init__(self, dados_json):
        self.raiz = self._construir_arvore(dados_json)

    def _construir_arvore(self, dados, pai=None):
        nome = dados.get("nome")
        tipo = dados.get("tipo")
        tamanho = dados.get("tamanho")
        
        no = No(nome, tipo, tamanho, pai)
        
        if "filhos" in dados:
            for filho_dados in dados["filhos"]:
                no.adicionar_filho(self._construir_arvore(filho_dados, no))
        return no


    def pre_ordem(self, no=None, resultado=None):
        if no is None:
            no = self.raiz
        if resultado is None:
            resultado = []
        
        resultado.append(no)
        for filho in no.filhos:
            self.pre_ordem(filho, resultado)
        return resultado

    def pos_ordem(self, no=None, resultado=None):
        if no is None:
            no = self.raiz
        if resultado is None:
            resultado = []
        
        for filho in no.filhos:
            self.pos_ordem(filho, resultado)
        resultado.append(no)
        return resultado

    def buscar(self, nome, no=None):
        if no is None:
            no = self.raiz
        if no.nome.lower() == nome.lower():
            return no
        for filho in no.filhos:
            res = self.buscar(nome, filho)
            if res:
                return res
        return None


    def altura(self, no=None):
        if no is None:
            no = self.raiz
        if not no.filhos:
            return 0
        return 1 + max(self.altura(filho) for filho in no.filhos)


    def profundidade(self, no):
        prof = 0
        atual = no
        while atual.pai is not None:
            prof += 1
            atual = atual.pai
        return prof


    def mostrar_folhas(self, no=None, folhas=None):
        if no is None:
            no = self.raiz
        if folhas is None:
            folhas = []
            
        if not no.filhos:
            folhas.append(no)
        else:
            for filho in no.filhos:
                self.mostrar_folhas(filho, folhas)
        return folhas


    def caminho(self, no):
        elementos = []
        atual = no
        while atual is not None:
            elementos.insert(0, atual.nome)
            atual = atual.pai
        return " / ".join(elementos)


    def calcular_tamanho(self, no):
        if no.tipo == "arquivo":
            return no.tamanho if no.tamanho else 0
        
        total = 0
        for filho in no.filhos:
            total += self.calcular_tamanho(filho)
        return total


    def buscar_por_extensao(self, extensao, no=None, encontrados=None):
        if no is None:
            no = self.raiz
        if encontrados is None:
            encontrados = []
            
        if no.tipo == "arquivo" and no.nome.endswith(extensao):
            encontrados.append(no)
        
        for filho in no.filhos:
            self.buscar_por_extensao(extensao, filho, encontrados)
        return encontrados


    def estatisticas(self):
        todos = self.pre_ordem()
        total_dirs = sum(1 for n in todos if n.tipo == "diretorio")
        total_arq = sum(1 for n in todos if n.tipo == "arquivo")
        tamanho_total = sum(n.tamanho for n in todos if n.tipo == "arquivo" and n.tamanho)
        
        print("\n--- ESTATÍSTICAS DA ÁRVORE ---")
        print(f"Total de Diretórios: {total_dirs}")
        print(f"Total de Arquivos: {total_arq}")
        print(f"Tamanho Total Ocupado: {tamanho_total:,} bytes")
        print(f"Altura da Árvore: {self.altura()}")

    def diretorio_maior_numero_arquivos(self):
        diretorios = [n for n in self.pre_ordem() if n.tipo == "diretorio"]
        if not diretorios:
            return None
        
        def contar_arquivos_abaixo(no):
            return sum(1 for n in self.pre_ordem(no) if n.tipo == "arquivo")

        melhor_dir = max(diretorios, key=contar_arquivos_abaixo)
        return melhor_dir, contar_arquivos_abaixo(melhor_dir)

if __name__ == "__main__":
    dados_json = {
      "nome": "usuario",
      "tipo": "diretorio",
      "filhos": [
        {
          "nome": "documentos",
          "tipo": "diretorio",
          "filhos": [
            {
              "nome": "faculdade",
              "tipo": "diretorio",
              "filhos": [
                {
                  "nome": "algoritmos",
                  "tipo": "diretorio",
                  "filhos": [
                    {"nome": "estruturas.py", "tipo": "arquivo", "tamanho": 12500},
                    {"nome": "arvores.pdf", "tipo": "arquivo", "tamanho": 850000},
                    {"nome": "grafos.pdf", "tipo": "arquivo", "tamanho": 920000}
                  ]
                },
                {
                  "nome": "banco_de_dados",
                  "tipo": "diretorio",
                  "filhos": [
                    {"nome": "modelo_er.pdf", "tipo": "arquivo", "tamanho": 480000},
                    {"nome": "consultas.sql", "tipo": "arquivo", "tamanho": 8300}
                  ]
                },
                {"nome": "horarios.txt", "tipo": "arquivo", "tamanho": 2100}
              ]
            },
            {
              "nome": "trabalho",
              "tipo": "diretorio",
              "filhos": [
                {"nome": "relatorio.docx", "tipo": "arquivo", "tamanho": 135000},
                {"nome": "apresentacao.pptx", "tipo": "arquivo", "tamanho": 2450000},
                {"nome": "dados.csv", "tipo": "arquivo", "tamanho": 78500}
              ]
            },
            {"nome": "notas.txt", "tipo": "arquivo", "tamanho": 3200}
          ]
        },
        {
          "nome": "imagens",
          "tipo": "diretorio",
          "filhos": [
            {
              "nome": "viagens",
              "tipo": "diretorio",
              "filhos": [
                {"nome": "serra.jpg", "tipo": "arquivo", "tamanho": 3250000},
                {"nome": "praia.jpg", "tipo": "arquivo", "tamanho": 2980000},
                {"nome": "cidade.png", "tipo": "arquivo", "tamanho": 1750000}
              ]
            },
            {"nome": "perfil.png", "tipo": "arquivo", "tamanho": 580000},
            {"nome": "logo.svg", "tipo": "arquivo", "tamanho": 42500}
          ]
        },
        {
          "nome": "downloads",
          "tipo": "diretorio",
          "filhos": [
            {
              "nome": "programas",
              "tipo": "diretorio",
              "filhos": [
                {
                  "nome": "editores",
                  "tipo": "diretorio",
                  "filhos": [
                    {"nome": "editor.zip", "tipo": "arquivo", "tamanho": 12500000}
                  ]
                },
                {"nome": "utilitario.zip", "tipo": "arquivo", "tamanho": 8750000}
              ]
            },
            {
              "nome": "livros",
              "tipo": "diretorio",
              "filhos": [
                {"nome": "python.pdf", "tipo": "arquivo", "tamanho": 5600000},
                {"nome": "algoritmos.pdf", "tipo": "arquivo", "tamanho": 7200000},
                {"nome": "redes.pdf", "tipo": "arquivo", "tamanho": 4300000}
              ]
            },
            {"nome": "manual.pdf", "tipo": "arquivo", "tamanho": 1500000}
          ]
        },
        {
          "nome": "projetos",
          "tipo": "diretorio",
          "filhos": [
            {
              "nome": "projeto_python",
              "tipo": "diretorio",
              "filhos": [
                {"nome": "main.py", "tipo": "arquivo", "tamanho": 5400},
                {"nome": "arvore.py", "tipo": "arquivo", "tamanho": 8700},
                {"nome": "README.md", "tipo": "arquivo", "tamanho": 2600}
              ]
            },
            {
              "nome": "projeto_web",
              "tipo": "diretorio",
              "filhos": [
                {"nome": "index.html", "tipo": "arquivo", "tamanho": 9200},
                {"nome": "estilo.css", "tipo": "arquivo", "tamanho": 6100},
                {"nome": "app.js", "tipo": "arquivo", "tamanho": 11400}
              ]
            }
          ]
        },
        {
          "nome": "temporario",
          "tipo": "diretorio",
          "filhos": []
        },
        {
          "nome": "configuracoes",
          "tipo": "diretorio",
          "filhos": [
            {"nome": "preferencias.json", "tipo": "arquivo", "tamanho": 1800}
          ]
        }
      ]
    }

    arvore = ArvoreArquivos(dados_json)

    while True:
        print("\n============== ÁRVORE DE ARQUIVOS ==============")
        print("1 - Mostrar árvore em pré-ordem")
        print("2 - Mostrar árvore em pós-ordem")
        print("3 - Buscar arquivo ou diretório")
        print("4 - Mostrar altura da árvore")
        print("5 - Consultar profundidade")
        print("6 - Mostrar folhas")
        print("7 - Mostrar caminho de um elemento")
        print("8 - Calcular tamanho de um diretório")
        print("9 - Buscar arquivos por extensão")
        print("10 - Mostrar estatísticas")
        print("11 - Diretório com maior número de arquivos")
        print("0 - Encerrar")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            print("\n--- Pré-ordem ---")
            for no in arvore.pre_ordem():
                print(f"[{no.tipo.upper()}] {no.nome}")
                
        elif opcao == "2":
            print("\n--- Pós-ordem ---")
            for no in arvore.pos_ordem():
                print(f"[{no.tipo.upper()}] {no.nome}")
                
        elif opcao == "3":
            nome = input("Digite o nome do arquivo ou diretório para buscar: ")
            res = arvore.buscar(nome)
            if res:
                print(f"Encontrado! Nome: {res.nome}, Tipo: {res.tipo}, Tamanho: {res.tamanho}")
            else:
                print("Elemento não encontrado.")
                
        elif opcao == "4":
            print(f"\nAltura da árvore: {arvore.altura()}")
            
        elif opcao == "5":
            nome = input("Digite o nome do elemento para ver a profundidade: ")
            res = arvore.buscar(nome)
            if res:
                print(f"A profundidade de '{res.nome}' é: {arvore.profundidade(res)}")
            else:
                print("Elemento não encontrado.")
                
        elif opcao == "6":
            print("\n--- Folhas da Árvore ---")
            for f in arvore.mostrar_folhas():
                print(f"-> {f.nome} ({f.tipo})")
                
        elif opcao == "7":
            nome = input("Digite o nome do elemento para ver o caminho: ")
            res = arvore.buscar(nome)
            if res:
                print(f"Caminho: {arvore.caminho(res)}")
            else:
                print("Elemento não encontrado.")
                
        elif opcao == "8":
            nome = input("Digite o nome do diretório: ")
            res = arvore.buscar(nome)
            if res and res.tipo == "diretorio":
                tam = arvore.calcular_tamanho(res)
                print(f"O tamanho total do diretório '{res.nome}' é {tam:,} bytes.")
            else:
                print("Diretório não encontrado ou o elemento é um arquivo.")
                
        elif opcao == "9":
            ext = input("Digite a extensão (ex: .pdf, .py): ")
            res = arvore.buscar_por_extensao(ext)
            if res:
                print(f"\nArquivos com a extensão '{ext}':")
                for arq in res:
                    print(f"- {arq.nome} ({arq.tamanho} bytes)")
            else:
                print("Nenhum arquivo encontrado com essa extensão.")
                
        elif opcao == "10":
            arvore.estatisticas()
            
        elif opcao == "11":
            dir_maior, qtd = arvore.diretorio_maior_numero_arquivos()
            if dir_maior:
                print(f"\nO diretório com mais arquivos é '{dir_maior.nome}' com {qtd} arquivos internos.")
            else:
                print("Nenhum diretório encontrado.")
                
        elif opcao == "0":
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")