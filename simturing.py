#Autores: Alberto Gusmão e Gabriel Gondim

import argparse

from utils.Arquivo import Arquivo

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
group.add_argument('-s', dest='step',action='store_true',help='Step: mostra a execução passo a passo')
group.add_argument('-step', dest='step',action='store_true',help='Step: mostra a execução passo a passo')
group.add_argument('-v', type=int, dest='verbose',help='Verbose numerado: mostra n linhas de execução passo a passo e depois para.')
group.add_argument('-verbose', type=int ,dest='verbose',help='Verbose numerado: mostra n linhas de execução passo a passo e depois para.')
args = parser.parse_args()

# ------------------------ Simulador ----------------------------------------
print('Simulador de Máquina de Turing ver 1.0 - IFMG 2023')
print('Desenvolvido como trabalho prático para a disciplina de Teoria da Computação')
print('Autores: Alberto Gusmão e Gabriel Gondim')

palavra = input('\nForneça a palavra inicial: ')
listaCaracteres = list(palavra)
listaCaracteres = [elemento.strip() for elemento in listaCaracteres if elemento.strip()]

print(listaCaracteres)
Arquivo(args.filename).lerArquivo()


while True:
    if args.resume: #Mostra conteudo final da fita e mata o programa
        print('Mostrando o conteúdo somente no final da fita')
        break
    elif args.step: #faz uma execução linha a linha e mata o programa
        print('Execução passo a passo')
        break
    elif args.verbose: #usuario define quantidade de passos, depois abre um prompt pedindo outras opções
        if args.verbose == -1:
            v = input('Defina a quantidade de passos: ')
            args.verbose = int(v)
        print(f'Rodando {args.verbose} linhas')
        args.verbose = False
    else: #prompt para o usuario escolher nova opção
        while True:
            op = input('Forneça opção (r,v,s): ')
            match op:
                case 'r':
                    args.resume = True
                    args.verbose = None
                    args.step = None
                    break
                case 'v':
                    args.resume = None
                    args.verbose = -1
                    args.step = None
                    break
                case 's':
                    args.resume = None
                    args.verbose = None
                    args.step = True
                    break
                case _:
                    print('Opção inválida !')




