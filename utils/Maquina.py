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
        if len(entrada) == 0:
            self.ponteiro = 0
            self.entrada = "_"
        else:
            self.ponteiro = int(entrada.find(entrada[0]))
        self.blocoAtual = "main"
        self.estadoAtual = '0'
        self.listaRetorno = []
        self.blocoAnterior = None
        self.estadoAnterior = None
        self.estadoFinal = False
        self.estadoPosRetorne = None
        self.pausa = None
        self.pausaPosBloco = None
        self.simboloVerificado = 0
        #delimitador do cabeçote
        if delim:
            self.delim = delim
        else: #delimitador padrão
            self.delim = '()'

    def run(self,debug=False,step=False):
        # i = contador de passos, começo em 2, pois já vou imprimir o primeiro passo antes de entrar no loop
        i = 0
        while not self.estadoFinal:

            if self.pausaPosBloco:
                self.pausaPosBloco = None
                return

            while self.estadoAtual == 'retorne':
                self.estadoAtual = self.listaRetorno[-1]["estadoPosRetorne"]
                self.blocoAnterior = self.blocoAtual
                self.blocoAtual = self.listaRetorno[-1]["blocoAnterior"]
                if self.listaRetorno[-1]["pausa"]:
                    return
                self.listaRetorno.pop()
                if debug:
                    print(self)
                i+=1

            if step and i >= step:
                return

            for elementos in self.banco:
                self.simboloVerificado = 0
                if (elementos["nome"] == self.blocoAtual):

                    for dados in elementos["dados"]:

                        if self.estadoAtual == "pare":
                            print(self)
                            exit()

                        if self.simboloVerificado == 0:
                            if self.verificaTransicao():
                                self.simboloVerificado = 1
                            else:
                                print(f"({self.estadoAtual},{dados['simboloAtual']}).Erro, não existe transição para esse simbolo. ")
                                exit()

                        if dados["estadoAtual"] == self.estadoAtual:
                            if len(dados) == 5 or len(dados) == 6:
                                if dados["simboloAtual"] == self.entrada[self.ponteiro] or dados["simboloAtual"] == "*":

                                    self.estadoAnterior = dados["estadoAtual"]
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
                                        self.estadoAtual = self.listaRetorno[-1]["estadoPosRetorne"]
                                        self.blocoAnterior = self.blocoAtual
                                        self.blocoAtual = self.listaRetorno[-1]["blocoAnterior"]
                                        if self.listaRetorno[-1]["pausa"]:
                                            self.pausaPosBloco = True
                                        self.listaRetorno.pop()

                                        if debug:
                                            print(self)
                                            i+=1

                                        if len(dados) == 6:
                                            return
                                        break
                                    else:
                                        if len(dados) == 6:
                                            return

                                    if debug:
                                        print(self)

                                    if step and i >= step:
                                        return

                                    #conta um passo realizado
                                    i+=1
                                    break

                            if len(dados) == 3 or len(dados) == 4:
                                self.estadoAnterior = dados["estadoAtual"]
                                #Obtendo o estado inicial do bloco
                                for bloco in self.banco:
                                    if bloco["nome"] == dados["bloco"]:
                                        self.estadoAtual = bloco["estadoInicial"]
                                        break
                                self.estadoPosRetorne = dados["comandoNovoEstado"]
                                # self.estadoAtual = elementos["estadoInicial"]
                                self.blocoAtual = dados["bloco"]
                                self.blocoAnterior = elementos["nome"]

                                if len(dados) == 4:
                                    self.pausa = dados["pausa"]

                                self.listaRetorno.append(
                                    {"estadoAnterior": self.estadoAnterior, "estadoPosRetorne": self.estadoPosRetorne,
                                     "blocoAtual": self.blocoAtual, "blocoAnterior": self.blocoAnterior, "pausa": self.pausa})

                                self.pausa = None

                                if debug:
                                    print(self)

                                if step and step <= i:
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

    def verificaTransicao(self):
        for elementos in self.banco:
            if elementos["nome"] == self.blocoAtual:
                for dados in elementos["dados"]:
                    if dados['estadoAtual'] == self.estadoAtual or dados['estadoAtual'] == 'retorne':
                        if len(dados) == 5 or len(dados) == 6:
                            if dados["simboloAtual"] == self.entrada[self.ponteiro] or dados["simboloAtual"] == '*':
                                return True
                        if len(dados) == 3 or len(dados) == 4:
                                return True

        return False