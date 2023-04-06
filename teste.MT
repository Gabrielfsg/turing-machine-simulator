; Detector de palindromos
 bloco main 1

     01 a −− A i 10
     01 b −− B i 20
     20 moveFim 21
     10 moveFim 11

     ; l e u a
     11 iniEsq 12
     12 a −− A i 30
     12 b −− * i 70
     12 _ −− * d 60
     ;MAIN 12 VE '_', vai pro 60

     ; leu b
     21 iniEsq 22
     22 a −− * i 70
     22 b −− B i 30
     22 _ −− * d 60

     30 moveIni 31
     31 iniDir 32
     32 _ −− * e 60
     32 * −− * i 01

     60 sim pare
     70 nao pare
 fim ; main

 ; palavra eh palindromo
 bloco sim 1
     01 moveFim 02
     02 * −− * d 03
     03 _ −− S d 04
     04 _ −− I d 05
     05 _ −− M d retorne
 fim ; sim

 ; move para ultimo caractere da palavra
 bloco moveFim 1
     01 _ −− * e retorne
     01 * −− * d 01
 fim ; moveFim

 ; move para primeiro caractere da palavra
 bloco moveIni 1
     01 _ −− * d retorne
     01 * −− * e 01
 fim ; moveIni

 bloco  iniEsq 1
     ;recua ate caractere minusculo ou _
     ;VEM AQUI, RETORNA NA MAIN 12
     01 _ −− * i retorne
     01 a −− * i retorne
     01 b −− * i retorne
     01 * −− * e 01
 fim ; iniEsq

 ; avanca ate caractere minusculo ou _
 bloco iniDir 1
     01 _ −− * i retorne
     01 a −− * i retorne
     01 b −− * i retorne
     01 * −− * d 01
 fim ; inidir

 ; palavra nao eh palindromo
    bloco nao 1
    01 moveFim 02
    02 * −− * d 03
    03 _ −− N d 04
    04 _ −− A d 05
    05 _ −− O d retorne
fim ; nao