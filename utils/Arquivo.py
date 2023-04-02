#Autores: Alberto Gusmão e Gabriel Gondim

class Arquivo():

    def __init__(self, arquivo):
        self.arquivo = arquivo

    def lerArquivo(self,mt):
        with open(self.arquivo,encoding='utf-8') as arq:
            lendoBloco = False
            linhaNum = 1
            for linha in arq:
                linha = linha.strip()
                if not linha.startswith(';') and linha != '': #ignoro os comentários
                       if linha.startswith('bloco'):
                           _,bloco,estadoInicial = linha.split()
                           mt.criaBloco(bloco,estadoInicial)
                           lendoBloco = True
                       if linha.startswith('fim'):
                           lendoBloco = False
                       if lendoBloco and not linha.startswith('bloco'):
                           cmd = linha.split()

                           if len(cmd) == 3: #transicao com chamada de outro bloco
                               estadoAtual,novoBloco,novoEstado = cmd
                               mt.criaTransicao(linhaNum,bloco,estadoAtual,novoEstado,novoBloco=novoBloco)
                           elif len(cmd) == 4 and cmd[-1] == '!': #transicao com chamada de outro bloco com breakpoint
                               estadoAtual,novoBloco,novoEstado,_ = cmd
                               mt.criaTransicao(linhaNum,bloco,estadoAtual,novoEstado,novoBloco=novoBloco,breakpoint=True)
                           elif len(cmd) == 6: #transicao normal dentro do bloco atual
                               estadoAtual,simboloAtual,_,novoSimbolo,movimento,novoEstado = cmd
                               mt.criaTransicao(linhaNum,bloco,estadoAtual,novoEstado,simboloAtual,novoSimbolo,movimento)
                           elif len(cmd) == 7 and cmd[-1] == '!':  # transicao normal dentro do bloco atual com BREAKPOINT
                               estadoAtual, simboloAtual, _, novoSimbolo, movimento, novoEstado, _ = cmd
                               mt.criaTransicao(linhaNum, bloco, estadoAtual, novoEstado, simboloAtual, novoSimbolo,
                                                movimento,breakpoint=True)
                           else:
                               print(f'Linha[{linhaNum}]: Sintaxe do comando [{linha}] inválida !')
                               exit(1)

                linhaNum = linhaNum + 1


