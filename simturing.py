import argparse

from Arquivo import Arquivo

#Argumentos necessários pro programa
"""

-resume (ou -r), executa o programa até o fim e depois imprime o conteúdo final na fita.
-verbose (ou -v) execução passo a passo
-step <n> (ou -s <n>) mostra n linhas de execução passo a passo na tela, depois abre o prompt pedindo nova opção 
(r,v,s). Se não fornecer nenhuma opção, repete-se a última opção

"""

# parser = argparse.ArgumentParser(description='Simulador de Máquina de Turing ver 1.0 - IFMG 2023')
# parser.add_argument('-r', '--arg1', help='Resume')
# parser.add_argument('-s', '--arg2', help='Verbose')
# parser.add_argument('-v', '--arg2', help='Verbose numerado')
# args = parser.parse_args()


print('Simulador de Máquina de Turing ver 1.0 - IFMG 2023')
print('Desenvolvido como trabalho prático para a disciplina de Teoria da Computação')
print('Autores: Alberto Gusmão e Gabriel Gondim')

print('\nForneça a palavra inicial: ',end='')
palavra = input()

Arquivo("teste.MT").lerArquivo()



