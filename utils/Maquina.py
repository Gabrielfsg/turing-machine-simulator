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

    def __init__(self,delim='()'):

        self.fita = ''
        #Usados pra imprimir a saida
        self.bloco = dict()
        self.blocoAtual = 'main'
        self.cabecote = 0
        self.estadoAtual = 1
        #Usados no processamento da palavra
        self.simboloAtual = None
        self.novoSimbolo = None
        self.movimento = None
        self.novoEstado = None
        self.transicoes = dict()
        #delimitador do cabeçote
        self.delim = delim

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
                print(f'Linha[{linha}]: Novo estado [{estadoNovo}]deve ser um inteiro de até 4 dígitos !')
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
        #Setup inicial, bloco main, estado 1, primeira letra do cabeçote
        self.fita = palavra

        if debug:
            print(self) #printando configuração inicial da maquina

        self.mover(debug)

    def obterSimboloAtual(self): #verificando se há transição pro caractere que está no cabeçote

        if not self.saiuFita():
            charCabecote = self.fita[self.cabecote]
            if self.transicoes.get((self.blocoAtual,int(self.estadoAtual),charCabecote)):
                return charCabecote
            elif self.transicoes.get((self.blocoAtual,int(self.estadoAtual),'*')):
                return '*'
            elif self.transicoes.get((self.blocoAtual,int(self.estadoAtual),'_')):
                return '_'
            elif self.transicoes.get((self.blocoAtual,int(self.estadoAtual))): #É chamada de bloco, retonar o proprio caractere
                return charCabecote
            else:
                print('Não foi possível encontrar transições para o símbolo atual na fita')
                exit(1)
        else:
            return '_'

    def mover(self,debug):
        parar = False
        while not parar:
            res = None
            try:
                self.simboloAtual = self.obterSimboloAtual()
                res = self.transicoes[(self.blocoAtual,int(self.estadoAtual),self.simboloAtual)]
                s,m,e = res
                if s != '*':
                    lista = list(self.fita)
                    lista[self.cabecote] = s
                    self.fita = "".join(lista)

                match m:
                    case 'd':
                        self.cabecote+=1
                    case 'e':
                        self.cabecote-=1

                if e == 'pare':
                    print(self)
                    break
                    parar = True

                elif e == 'retorne':
                    return
                else:
                    self.estadoAtual = e

                if debug:
                    print(self)

            except Exception as a:
                try:
                    blocoBkp = self.blocoAtual

                    #chamada de bloco
                    res = self.transicoes[(self.blocoAtual,int(self.estadoAtual))]
                    b,e = res

                    self.blocoAtual = b
                    self.estadoAtual = self.bloco[b]

                    self.mover(debug)

                    #Voltando ao setup anterior de quem chamou o bloco
                    self.blocoAtual = blocoBkp
                    self.estadoAtual = e
                except Exception:
                    print(f'Não foi possível encontrar uma transição para o bloco {self.blocoAtual} e estado {self.estadoAtual}')
                    exit(1)

            # print(f'res: {res}')
    def criaBloco(self,b,estadoInicial):
        if b in self.bloco.keys():
            print(f'Bloco {b} já existe !')
            exit(1)
        self.bloco[b] = estadoInicial

    def saiuFita(self):
        if self.cabecote < len(self.fita):
            if self.cabecote < 0: #saiu pela esquerda
                return True
        else: #saiu pela direita
            return True
        return False

    def __str__(self):
        #bloco e estado atual
        s = f"{self.blocoAtual.rjust(16,'.')}.{'{:04d}'.format(int(self.estadoAtual))}: "
        #formatando saídas: cabeçote, parte esquerda da fita e parte direita da fita

        if self.saiuFita(): #Saiu da palavra
            simb = '_'
        else:
            simb = self.fita[self.cabecote]

        cabecote = f"{self.delim[0]}{simb}{self.delim[1]}"
        s += f"{self.fitaEsquerda()}{cabecote}{self.fitaDireita()}"
        return s

    def fitaEsquerda(self):
        max_len = 20
        fitaEsq = ''
        if self.cabecote > 0:
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

    def printTransicoes(self):
        for keys in self.transicoes.keys():
            if len(keys) == 3: #comando comum
                b,e,s = keys
                d = self.transicoes[(b,e,s)]
                print(f'Instrução de bloco: ({b},{e},{s}) => {d}')
            if len(keys) == 2: #comando de chamada de bloco
                b,e = keys
                d = self.transicoes[(b,e)]
                print(f'Chamando bloco: ({b},{e}) => {d}')