#Autores: Alberto Gusmão e Gabriel Gondim

import argparse

from utils.Arquivo import Arquivo
from utils.Maquina import Maquina

#Argumentos necessários pro programa
"""

-resume (ou -r), executa o programa até o fim e depois imprime o conteúdo final na fita.
-verbose (ou -v) execução passo a passo
-step <n> (ou -s <n>) mostra n linhas de execução passo a passo na tela, depois abre o prompt pedindo nova opção 
(r,v,s). Se não fornecer nenhuma opção, repete-se a última opção

"""

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
parser.add_argument('filename', help='Arquivo .MT')
parser.add_argument('-head', dest='head',type=str, help='Customiza delimitadores do cabeçote')
group.add_argument('-r', dest='resume', action='store_true',help='Resume: executa o programa até o fim e depois imprime o conteúdo final na fita')
group.add_argument('-resume',dest='resume', action='store_true',help='Resume: executa o programa até o fim e depois imprime o conteúdo final na fita')
group.add_argument('-s', dest='step',type=int,help='Step: mostra a execução passo a passo com n linhas')
group.add_argument('-step', dest='step',type=int,help='Step: mostra a execução passo a passo com n linhas')
group.add_argument('-v', action='store_true', dest='verbose',help='Verbose numerado:  linhas de execução passo a passo e depois para.')
group.add_argument('-verbose',action='store_true',dest='verbose',help='Verbose numerado:  linhas de execução passo a passo e depois para.')
args = parser.parse_args()

# ------------------------ Simulador ----------------------------------------
print('Simulador de Máquina de Turing ver 1.0 - IFMG 2023')
print('Desenvolvido como trabalho prático para a disciplina de Teoria da Computação')
print('Autores: Alberto Gusmão e Gabriel Gondim')

palavra = input('\nForneça a palavra inicial: ')
# args.filename
banco = Arquivo(args.filename).lerArquivo()
mt = Maquina(banco,palavra,args.head)
#Imprime configuração inicial
print('Configuração incial: ')
print(mt)
while True:
    if args.resume: #Mostra conteudo final da fita e mata o programa
        print('Mostrando o conteúdo somente no final da fita')
        args.resume = False
        mt.run()
    elif args.verbose: #faz uma execução linha a linha e mata o programa
        print('Execução passo a passo')
        args.verbose = False
        mt.run(debug=True)
    elif args.step: #usuario define quantidade de passos, depois abre um prompt pedindo outras opções
        if args.step == -1:
            v = input('Defina a quantidade de passos: ')
            args.step = int(v)
        print(f'Rodando {args.step} linhas')
        mt.run(debug=True,step=args.step)
        args.step = False
    else: #prompt para o usuario escolher nova opção
        while True:
            op = input('Forneça opção (r,v,s): ')
            match op:
                case 'r':
                    args.resume = True
                    args.step = None
                    args.verbose = None
                    break
                case 'v':
                    args.resume = None
                    args.step = None
                    args.verbose = True
                    break
                case 's':
                    args.resume = None
                    args.step = -1
                    args.verbose = None
                    break
                case _:
                    print('Opção inválida !')




