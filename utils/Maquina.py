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

    def __init__(self,palavra,delim = '()'):
        self.fita = palavra

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
        self.delim = delim

    def criaTransicao(self,linha,bloco,estadoAtual,novoEstado,
    simboloAtual=None,novoSimbolo=None,movimento=None,novoBloco=None,breakpoint=False):

        erro = False
        if novoBloco is None:
            if len(bloco) > 16:
                print(f'Linha[{linha}]: Nome do bloco [{bloco}] excede 16 caracteres !')
                erro = True
            if int(estadoAtual) > 9999:
                print(f'Linha[{linha}]: Estado atual [{estadoAtual}]deve ser um inteiro de até 4 dígitos !')
                erro = True
            if int(novoEstado) > 9999 and (estadoAtual != 'pare' or estadoAtual != 'retorne'):
                print(f'Linha[{linha}]: Novo estado [{novoEstado}]deve ser um inteiro de até 4 dígitos !')
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
        else:
            if len(novoBloco) > 16:
                print(f'Linha[{linha}]: Nome do bloco de chamada [{novoBloco}] excede 16 caracteres !')
                erro = True
            if int(estadoAtual) > 9999:
                print(f'Linha[{linha}]: Estado atual [{estadoAtual}]deve ser um inteiro de até 4 dígitos !')
                erro = True
            if int(novoEstado) > 9999 and (estadoAtual != 'pare' or estadoAtual != 'retorne'):
                print(f'Linha[{linha}]: Novo estado [{novoEstado}]deve ser um inteiro de até 4 dígitos !')
                erro = True


        if erro:
            print('Simulação encerrada com erros nas transições')
            exit(1)

        if novoBloco is None:
            self.transicoes[(bloco,estadoAtual,simboloAtual)] = (novoSimbolo,movimento,novoEstado)
        else:
            self.transicoes[(bloco,estadoAtual)] = (novoBloco,novoEstado)
    def criaBloco(self,b,estadoInicial):
        if b in self.bloco.keys():
            print(f'Bloco {b} já existe !')
            exit(1)
        self.bloco[b] = estadoInicial

    def printTransicoes(self):
        print('Imprimindo transicoes')
        for (b,e,s) in self.transicoes.keys():
            d = self.transicoes[(b,e,s)]
            print(f'({b},{e},{s}) => ({d})')

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