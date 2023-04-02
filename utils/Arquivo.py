#Autores: Alberto Gusmão e Gabriel Gondim

class Arquivo():

    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.texto = []

    def lerArquivo(self):
        with open(self.arquivo) as arq:
            for linha in arq:
                linha = linha.strip()
                self.texto.append(linha)

    def removeComentarios(texto):
        for linha in texto:
            if linha.startswith(";"):
                texto.remove(linha)
        return texto

