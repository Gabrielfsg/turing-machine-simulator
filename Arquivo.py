class Arquivo():

    def __init__(self, arquivo):
        self.arquivo = arquivo

    def lerArquivo(self):
        texto = []
        with open(self.arquivo) as arq:
            for linha in arq:
                linha = linha.strip()
                texto.append(linha)
        print(texto)


    def removeComentarios(texto):
        for linha in texto:
            if linha.startswith(";"):
                texto.remove(linha)
        return texto

