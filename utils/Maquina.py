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

    def __init__(self):

        self.fita = ''
        #Usados pra imprimir a saida
        self.bloco = dict()
        self.cabecote = 0
        self.estadoAtual = None
        #Usados no processamento da palavra
        self.simboloAtual = None
        self.novoSimbolo = None
        self.movimento = None
        self.novoEstado = None
        self.transicoes = dict()
        #delimitador do cabeçote
        self.delim = None

    def criaTransicao(self,linha,bloco,estadoAtual,estadoNovo,
    simboloAtual=None,novoSimbolo=None,movimento=None,novoBloco=None,breakpoint=False):

        erro = False
        if novoBloco is None: #verificar simbolos e movimento

            if len(bloco) > 16:
                print(f'Linha[{linha}]: Nome do bloco [{bloco}] excede 16 caracteres !')
                erro = True

            if len(simboloAtual) > 1:
                print(f'Linha[{linha}]: Simbolo atual [{simboloAtual}] inválido !')
                erro = True

            if len(novoSimbolo) > 1:
                print(f'Linha[{linha}]: Novo simbolo [{novoSimbolo}] inválido !')
                erro = True

            if movimento != 'i' and movimento != 'd' and movimento != 'e':
                print(f'Linha[{linha}]: Movimento [{movimento}] inválido !')
                erro = True
        else: #verificar nome do bloco de chamada
            if len(novoBloco) > 16:
                print(f'Linha[{linha}]: Nome do bloco de chamada [{novoBloco}] excede 16 caracteres !')
                erro = True

        #Analisando o estado atual informado e o novo estado
        if estadoAtual == 'pare' or estadoAtual == 'retorne':
            print(f'Linha[{linha}]: Estado atual [{estadoAtual}] deve possuir valor númerico!')
            erro = True
        else:
            if int(estadoAtual) > 9999:
                print(f'Linha[{linha}]: Estado atual [{estadoAtual}]deve ser um inteiro de até 4 dígitos !')
                erro = True

        if estadoNovo != 'pare' and estadoNovo != 'retorne':
            if int(estadoNovo) > 9999:
                print(f'Linha[{linha}]: Novo estado [{novoEstado}]deve ser um inteiro de até 4 dígitos !')
                erro = True

        if erro:
            print('Simulação encerrada com erros nas transições')
            exit(1)

        if novoBloco is None:
            if breakpoint:
                self.transicoes[(bloco,int(estadoAtual),simboloAtual)] = (novoSimbolo,movimento,estadoNovo,'!')
            else:
                self.transicoes[(bloco,int(estadoAtual),simboloAtual)] = (novoSimbolo,movimento,estadoNovo)
        else:
            if breakpoint:
                self.transicoes[(bloco,int(estadoAtual))] = (novoBloco,estadoNovo,'!')
            else:
                self.transicoes[(bloco,int(estadoAtual))] = (novoBloco,estadoNovo)

    def run(self,palavra,debug = True):
        #Setup inicial, bloco main, estado 1
        self.bloco = 'main'
        self.estadoAtual = 1
        self.fita = palavra
        self.cabecote = 0
        parar = False
        if debug:
            print(self) #printando configuração inicial da maquina
        while not parar:
            res = None
            try:
                res = self.transicoes[(self.bloco,self.estadoAtual,self.fita[self.cabecote])]
                s,m,e = res
                self.fita[self.cabecote] = s
                match m:
                    case 'd':
                        self.cabecote+=1
                    case 'e':
                        self.cabecote-=1

                if e == 'pare':
                    print(self)
                    print('Palavra aceita')
                    exit(0)
                elif e == 'retorne':
                    pass
                else:
                    self.estadoAtual = e

                if debug:
                    print(self)

            except Exception:
                try:
                    #chamada de bloco
                    res = self.transicoes[(self.bloco,self.estadoAtual)]
                    b,e = res
                    self.bloco = b
                    self.run(palavra)
                    self.estadoAtual = e
                except Exception:
                    print(f'Não foi possível encontrar uma transição para o bloco {self.bloco} e estado {self.estadoAtual}')
                    exit(1)

            # print(f'res: {res}')
    def criaBloco(self,b,estadoInicial):
        if b in self.bloco.keys():
            print(f'Bloco {b} já existe !')
            exit(1)
        self.bloco[b] = estadoInicial

    def printTransicoes(self):
        print('Imprimindo transicoes')
        for keys in self.transicoes.keys():
            if len(keys) == 3:
                b,e,s = keys
                d = self.transicoes[(b,e,s)]
                print(f'Instrução de bloco: ({b},{e},{s}) => ({d})')
            if len(keys) == 2:
                b,e = keys
                d = self.transicoes[(b,e)]
                print(f'Chamando bloco: ({b},{e}) => ({d})')

    def __str__(self):
        #bloco e estado atual
        s = f"{self.bloco.rjust(16,'.')}.{'{:04d}'.format(int(self.estadoAtual))}: "
        #formatando saídas: cabeçote, parte esquerda da fita e parte direita da fita
        cabecote = f"{self.delim[0]}{self.fita[self.cabecote]}{self.delim[1]}"
        s += f"{self.fitaEsquerda()}{cabecote}{self.fitaDireita()}"
        return s

    def fitaEsquerda(self):
        max_len = 20
        fitaEsq = self.fita[:self.cabecote][::-1][:20][::-1]
        while len(fitaEsq) < max_len:
            fitaEsq = '_' + fitaEsq
        return fitaEsq

    def fitaDireita(self):
        max_len = 20
        fitaDir = self.fita[self.cabecote+1:self.cabecote+20]
        while len(fitaDir) < max_len:
            fitaDir += '_'
        return fitaDir