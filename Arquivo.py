class Arquivo():

    def __init__(self, arquivo):
        self.arquivo = arquivo

    def lerArquivo(self):
        print(self.arquivo)
        with open(self.arquivo) as arq:
            for line in arq:
                print(line)
