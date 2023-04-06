# Autores: Alberto Gusmão e Gabriel Gondim

import codecs


class Arquivo():

    def __init__(self, arquivo,entrada):
        self.arquivo = arquivo
        self.entrada = entrada
        self.texto = None
        self.textoEmLinhas = None
        self.banco = []

    def lerArquivo(self):
        texto = []
        with codecs.open(self.arquivo, encoding='utf-8') as arq:
            self.texto = arq
            texto = self.separarTexto()
            self.textoEmLinhas = texto
            self.separarBlocos()
            self.executaArquivo()

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

    def executaArquivo(self):
        estadoFinal = False
        entrada = self.entrada
        ponteiro = int(entrada.find(entrada[0]))
        blocoAnterior = None
        blocoAtual = "main"
        estadoAtual = None
        estadoAnterior = None
        estadoPosRetorne = None
        listaRetorno = []
        passou = 0
        nExiste = 0
        while not estadoFinal:

            if passou == 0:
                nExiste += 1
                if nExiste == 2:
                    print("Erro, não existe transição para esse simbolo. ")
                    exit()
            for elementos in self.banco:
                if (elementos["nome"] == blocoAtual):
                    if estadoAtual is None:
                        estadoAtual = elementos["estadoInicial"]
                    for dados in elementos["dados"]:

                        if estadoAtual == "pare":
                            print(entrada)
                            exit()

                        if estadoAtual != "retorne" and int(dados["estadoAtual"]) == int(estadoAtual):
                            if len(dados) == 5:
                                if dados["simboloAtual"] == entrada[ponteiro] or dados["simboloAtual"] == "*":
                                    passou += 1
                                    estadoAnterior = dados["estadoAtual"]
                                    estadoAtual = dados["comandoNovoEstado"]
                                    if dados["novoSimbolo"] != "*":
                                        listaEntrada = list(entrada)
                                        listaEntrada[ponteiro] = dados["novoSimbolo"]
                                        entrada = "".join(listaEntrada)

                                    if dados["movimento"] == "e":
                                        if ponteiro == 0:
                                            entrada = "_" + entrada
                                        else:
                                            ponteiro = ponteiro - 1

                                    if dados["movimento"] == "d":
                                        if ponteiro == len(entrada) - 1:
                                            entrada = entrada + "_"
                                            ponteiro = ponteiro + 1
                                        else:
                                            ponteiro = ponteiro + 1

                                    if estadoAtual == "retorne":
                                        estadoAtual = listaRetorno[len(listaRetorno) - 1]["estadoPosRetorne"]
                                        blocoAnterior = blocoAtual
                                        blocoAtual = listaRetorno[len(listaRetorno) - 1]["blocoAnterior"]
                                        listaRetorno.pop()
                                        break


                                    break

                            if len(dados) == 3:
                                passou += 1
                                estadoAnterior = dados["estadoAtual"]
                                estadoPosRetorne = dados["comandoNovoEstado"]
                                estadoAtual = None
                                blocoAtual = dados["bloco"]
                                blocoAnterior = elementos["nome"]
                                listaRetorno.append(
                                    {"estadoAnterior": estadoAnterior, "estadoPosRetorne": estadoPosRetorne,
                                     "blocoAtual": blocoAtual, "blocoAnterior": blocoAnterior})

                                break


            if estadoFinal == True:
                break
