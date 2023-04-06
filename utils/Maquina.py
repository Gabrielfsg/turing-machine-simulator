#Autores: Alberto Gusmão e Gabriel Gondim

"""
    Configuração de entrada da maquina:

    <estado atual> <símbolo atual> - - <novo símbolo> <movimento> <novo estado>

    • Alternativamente, para denotar o <novo estado> você pode utilizar os identificadores “retorne”
    ou “pare”. Identificadores são case-sensitive.
    • Para denotar o <símbolo atual> e o <novo símbolo> você pode usar qualquer caractere, ou use
    ’_’ para representar o branco (espaço).

    • O <movimento> denota a ação do cabeçote na fita, indicada por um caractere: ’e’ denota movi-
    mento para a esquerda, ’d’ denota movimento para a direita, ’i’ denota ausência de movimento (imóvel).
    • Tudo depois de um ’;’ é tratado como comentário e ignorado.
    • A execução termina quanto a MT alcança o estado “pare” ou ocorre um erro.

    '!' no final da linha é breakpoint

    Configuração instantanea de saída da maquina:

    <bloco>.<estado>: <fita à esquerda><cabeçote><fita à direita>

    • <bloco> identificador do bloco em execução, máximo de 16 caracteres significativos.
    • <estado> número inteiro positivo, máximo de 9999 por bloco (4 dígitos).
    • <fita à esquerda> os 20 caracteres mais próximos do cabeçote (ou espaços) pela esquerda
    • <cabeçote> 3 caracteres: delimitador da esquerda, símbolo na fita, delimitador da direita.
    • <fita à direita> os 20 caracteres mais próximos do cabeçote (ou espaços) pela direita.
"""

class Maquina:

    def __init__(self,banco,entrada,delim):

        self.entrada = entrada
        self.banco = banco
        #Inicializando valores que serão exibidos na saída
        self.ponteiro = int(entrada.find(entrada[0]))
        self.blocoAtual = "main"
        self.estadoAtual = '01'
        self.listaRetorno = []
        self.blocoAnterior = None
        self.estadoAnterior = None
        self.estadoFinal = False
        self.estadoPosRetorne = None
        #delimitador do cabeçote
        if delim:
            self.delim = delim
        else: #delimitador padrão
            self.delim = '()'

    def run(self,debug=False,verbose=False):
        passou = 0
        nExiste = 0
        # i = contador de passos, começo em 2, pois já vou imprimir o primeiro passo antes de entrar no loop
        i = 2
        if debug:
            print(self)
        while not self.estadoFinal:

            if passou == 0:
                nExiste += 1
                if nExiste == 2:
                    print("Erro, não existe transição para esse simbolo. ")
                    exit()

            for elementos in self.banco:
                if (elementos["nome"] == self.blocoAtual):

                    for dados in elementos["dados"]:

                        if self.estadoAtual == "pare":
                            print(self)
                            exit()

                        if self.estadoAtual != "retorne" and int(dados["estadoAtual"]) == int(self.estadoAtual):
                            if len(dados) == 5:
                                if dados["simboloAtual"] == self.entrada[self.ponteiro] or dados["simboloAtual"] == "*":
                                    passou += 1
                                    estadoAnterior = dados["estadoAtual"]
                                    self.estadoAtual = dados["comandoNovoEstado"]
                                    if dados["novoSimbolo"] != "*":
                                        listaEntrada = list(self.entrada)
                                        listaEntrada[self.ponteiro] = dados["novoSimbolo"]
                                        self.entrada = "".join(listaEntrada)

                                    if dados["movimento"] == "e":
                                        if self.ponteiro == 0:
                                            self.entrada = "_" + self.entrada
                                        else:
                                            self.ponteiro = self.ponteiro - 1

                                    if dados["movimento"] == "d":
                                        if self.ponteiro == len(self.entrada) - 1:
                                            self.entrada = self.entrada + "_"
                                            self.ponteiro = self.ponteiro + 1
                                        else:
                                            self.ponteiro = self.ponteiro + 1

                                    if self.estadoAtual == "retorne":
                                        self.estadoAtual = self.listaRetorno[len(self.listaRetorno) - 1]["estadoPosRetorne"]
                                        blocoAnterior = self.blocoAtual
                                        self.blocoAtual = self.listaRetorno[len(self.listaRetorno) - 1]["blocoAnterior"]
                                        self.listaRetorno.pop()
                                        break

                                    if debug:
                                        print(self)

                                    if verbose and verbose == i:
                                        return

                                    #conta um passo realizado
                                    i+=1
                                    break

                            if len(dados) == 3:
                                passou += 1
                                self.estadoAnterior = dados["estadoAtual"]
                                self.estadoPosRetorne = dados["comandoNovoEstado"]
                                self.estadoAtual = elementos["estadoInicial"]
                                self.blocoAtual = dados["bloco"]
                                self.blocoAnterior = elementos["nome"]
                                self.listaRetorno.append(
                                    {"estadoAnterior": self.estadoAnterior, "estadoPosRetorne": self.estadoPosRetorne,
                                     "blocoAtual": self.blocoAtual, "blocoAnterior": self.blocoAnterior})

                                if debug:
                                    print(self)

                                if verbose and verbose == i:
                                    return

                                i+=1
                                break

            if self.estadoFinal:
                break

    def __str__(self):
        #bloco e estado atual

        try:
            estadoAtual = '{:04d}'.format(int(self.estadoAtual))
        except Exception:
            estadoAtual = self.estadoAtual

        s = f"{self.blocoAtual.rjust(16,'.')}.{estadoAtual}: "
        #formatando saídas: cabeçote, parte esquerda da fita e parte direita da fita
        cabecote = f"{self.delim[0]}{self.entrada[self.ponteiro]}{self.delim[1]}"
        s += f"{self.fitaEsquerda()}{cabecote}{self.fitaDireita()}"
        return s

    def fitaEsquerda(self):
        max_len = 20
        fitaEsq = self.entrada[:self.ponteiro][::-1][:20][::-1]
        while len(fitaEsq) < max_len:
            fitaEsq = '_' + fitaEsq
        return fitaEsq

    def fitaDireita(self):
        max_len = 20
        fitaDir = self.entrada[self.ponteiro+1:self.ponteiro+20]
        while len(fitaDir) < max_len:
            fitaDir += '_'
        return fitaDir

