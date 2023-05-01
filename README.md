# Turing Machine Simulator

Como rodar:

    python simturing.py \<opções> \<programa> 

## \<opções\>: Argumentos na linha de comando

-r ou -resume: imprime conteúdo final da fita e termina.

-v ou -verbose: imprime execução passo a passo
    
-s ou -step: imprime n passos de execução, necessário passar um número inteiro logo na frente do argumento. Exemplo: 
 
    python simturing.py -s(ou -step) 10 teste.MT.

## \<programa>: Path do arquivo com extensão .MT com o código que o simulador deve executar.

# Observações

Importante ressaltar que não é possível informar vários argumentos de uma só vez, 
é necessário enviar um argumento por vez. Caso queira executar seu programa de formas diferentes em tempo de execução,
utilize o -verbose.