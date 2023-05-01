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
        for index, linha in enumerate(self.textoEmLinhas):
            palavras = linha.split()
            if len(palavras) > 0 and not palavras[0].startswith(";"):
                if palavras[0] == "bloco":
                    if len(palavras[1]) > 16:
                        print('O bloco ' + str(palavras[0]) + ' possui mais de 16 caracteres. ')
                        exit()
                    if len(palavras) == 3:
                        blocoAtual = {"tipo": palavras[0], "nome": palavras[1], "estadoInicial": palavras[2], "dados": []}
                    elif len(palavras) > 3:
                        print('A linha ' + str(index+1) + ' não pode haver mais de 3 argumentos. ')
                        exit()
                elif not palavras[0] == ("bloco") and not palavras[0] == "fim" and (
                        len(palavras) == 3 or len(palavras) == 6 or len(palavras) == 4 or len(palavras) == 7):
                    if len(palavras) == 3 or len(palavras) == 4:
                        if int(palavras[0]) > 9999:
                            print('O estado ' + str(palavras[0]) + ' é um inteiro maior que 9999. Defina estados menor igual a 9999. ')
                            exit()
                        if len(palavras) == 3:
                            dadosBloco = {"estadoAtual": palavras[0], "bloco": palavras[1],
                                          "comandoNovoEstado": palavras[2]}
                            blocoAtual["dados"].append(dadosBloco)
                        if len(palavras) == 4:
                            if palavras[3] == "!":
                                dadosBloco = {"estadoAtual": palavras[0], "bloco": palavras[1],
                                              "comandoNovoEstado": palavras[2], "pausa": True}
                                blocoAtual["dados"].append(dadosBloco)
                            else:
                                self.erroArquivo(index + 1, palavras[3])
                    elif len(palavras) == 6 or len(palavras) == 7:
                        if int(palavras[0]) > 9999:
                            print('O estado ' + str(palavras[0]) + ' é um inteiro maior que 9999. Defina estados menor igual a 9999. ')
                            exit()
                        if len(palavras) == 6:
                            dadosBloco = {"estadoAtual": palavras[0], "simboloAtual": palavras[1],
                                          "novoSimbolo": palavras[3], "movimento": palavras[4],
                                          "comandoNovoEstado": palavras[5]}
                            blocoAtual["dados"].append(dadosBloco)

                        if len(palavras) == 7:
                            if palavras[6] == "!":
                                dadosBloco = {"estadoAtual": palavras[0], "simboloAtual": palavras[1],
                                              "novoSimbolo": palavras[3], "movimento": palavras[4],
                                              "comandoNovoEstado": palavras[5], "pausa": True}
                                blocoAtual["dados"].append(dadosBloco)
                            else:
                                self.erroArquivo(index + 1, palavras[6])

                elif palavras[0] == "fim":
                    self.banco.append(blocoAtual)
                    blocoAtual = None
                    dadosBloco = None
        return self.banco

    def erroArquivo(self, linha, elemento):
        print('Erro, o elemento ' + str(elemento) + ' na linha ' + str(linha) + ' não é aceito pelo programa. ')
        exit()

