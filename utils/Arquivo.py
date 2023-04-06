# Autores: Alberto Gusmão e Gabriel Gondim

import codecs


class Arquivo():

    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.texto = None
        self.textoEmLinhas = None
        self.banco = []

    def lerArquivo(self):
        texto = []
        with codecs.open(self.arquivo, encoding='utf-8') as arq:
            self.texto = arq
            texto = self.separarTexto()
            self.textoEmLinhas = texto
            return self.separarBlocos()

    def separarTexto(self):
        texto = []
        for linha in self.texto:
            linha = linha.strip()
            texto.append(linha)
        return texto

    def separarBlocos(self):
        blocoAtual = None
        dadosBloco = None
        for linha in self.textoEmLinhas:
            palavras = linha.split()
            if len(palavras) > 0 and not palavras[0].startswith(";"):
                if len(palavras) == 3 and palavras[0] == "bloco":
                    blocoAtual = {"tipo": palavras[0], "nome": palavras[1], "estadoInicial": palavras[2], "dados": []}
                elif not palavras[0] == ("bloco") and not palavras[0] == "fim" and (
                        len(palavras) == 3 or len(palavras) == 6):
                    if len(palavras) == 3:
                        dadosBloco = {"estadoAtual": palavras[0], "bloco": palavras[1],
                                      "comandoNovoEstado": palavras[2]}
                        blocoAtual["dados"].append(dadosBloco)
                    if len(palavras) == 6:
                        dadosBloco = {"estadoAtual": palavras[0], "simboloAtual": palavras[1],
                                      "novoSimbolo": palavras[3], "movimento": palavras[4],
                                      "comandoNovoEstado": palavras[5]}
                        blocoAtual["dados"].append(dadosBloco)
                elif palavras[0] == "fim":
                    self.banco.append(blocoAtual)
                    blocoAtual = None
                    dadosBloco = None

        return self.banco


