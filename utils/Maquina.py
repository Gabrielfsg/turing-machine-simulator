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

    def __init__(self,palavra,delim = False):
        self.fita = palavra

        #Usados pra imprimir a saida
        self.bloco = None
        self.cabecote = 0
        self.estadoAtual = None

        #Usados no processamento da palavra
        self.simboloAtual = None
        self.novoSimbolo = None
        self.movimento = None
        self.novoEstado = None

        #delimitador do cabeçote
        if delim == False:
            self.delim = '()'
        else:
            self.delim = delim

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