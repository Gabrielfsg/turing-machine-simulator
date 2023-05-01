; -- ALFABETO DA FITA --

;0=a
;1=b
;2=c
;3=d
;4=e
;5=f
;6=g
;7=h
;8=i
;9=j

;0+1 = 1=k
;1+1 = 2=l
;2+1 = 3=m
;3+1 = 4=n
;4+1 = 5=o
;5+1 = 6=p
;6+1 = 7=q
;7+1 = 8=r
;8+1 = 9=s
;9+1 = 0=t e u = 1

; -------------------

bloco main 1

    ;reseta = 10
    ;1ponto1 = 11
    ;numEsq = 12

    0 _ -- = i 10
    0 0 -- * d 0
    0 1 -- * d 0
    0 2 -- * d 0
    0 3 -- * d 0
    0 4 -- * d 0
    0 5 -- * d 0
    0 6 -- * d 0
    0 7 -- * d 0
    0 8 -- * d 0
    0 9 -- * d 0
    0 + -- * d 0
    0 * -- * i pare

    10 _ -- * d 1
    10 * -- * e 10

    1 0 -- * e 11
    1 1 -- * e 11
    1 2 -- * e 11
    1 3 -- * e 11
    1 4 -- * e 11
    1 5 -- * e 11
    1 6 -- * e 11
    1 7 -- * e 11
    1 8 -- * e 11
    1 9 -- * e 11
    1 t -- * e 11
    1 u -- * e 11
    1 k -- * e 11
    1 l -- * e 11
    1 m -- * e 11
    1 n -- * e 11
    1 o -- * e 11
    1 p -- * e 11
    1 q -- * e 11
    1 r -- * e 11
    1 s -- * e 11

    1 _ -- * d 3
    1 * -- * e 1

    11 _ -- * d 2
    11 * -- * e 11

    2 movDirNumEsq 12
    12 numEsq 1

    3 resPronto pare

fim

;pega o digito menos significativo do primeiro operando
bloco movDirNumEsq 1
    1 + -- * e retorne
    1 * -- * d 1
fim

;operações possíveis com os algarismos do primeiro operando
bloco numEsq 0

;1 = movDirNumDirOpe0
;2 = movDirNumDirOpe1
;3 = movDirNumDirOpe2
;4 = movDirNumDirOpe3
;5 = movDirNumDirOpe4
;6 = movDirNumDirOpe5
;7 = movDirNumDirOpe6
;8 = movDirNumDirOpe7
;9 = movDirNumDirOpe8
;10 = movDirNumDirOpe9

    0 0 -- a i 1
    0 1 -- b i 2
    0 2 -- c i 3
    0 3 -- d i 4
    0 4 -- e i 5
    0 5 -- f i 6
    0 6 -- g i 7
    0 7 -- h i 8
    0 8 -- i i 9
    0 9 -- j i 10

    0 t -- j i 1
    0 u -- _ i 2
    0 k -- a i 2
    0 l -- b i 3
    0 m -- c i 4
    0 n -- d i 5
    0 o -- e i 6
    0 p -- f i 7
    0 q -- g i 8
    0 r -- h i 9
    0 s -- i i 10

    0 _ -- * i 1
    0 * -- * e 0


;11 = somaNumEsq0
;12 = somaNumEsq1
;13 = somaNumEsq2
;14 = somaNumEsq3
;15 = somaNumEsq4
;16 = somaNumEsq5
;17 = somaNumEsq6
;18 = somaNumEsq7
;19 = somaNumEsq8
;20 = somaNumEsq9


    1 = -- * e 11
    1 * -- * d 1

    2 = -- * e 12
    2 * -- * d 2

    3 = -- * e 13
    3 * -- * d 3

    4 = -- * e 14
    4 * -- * d 4

    5 = -- * e 15
    5 * -- * d 5

    6 = -- * e 16
    6 * -- * d 6

    7 = -- * e 17
    7 * -- * d 7

    8 = -- * e 18
    8 * -- * d 8

    9 = -- * e 19
    9 * -- * d 9

    10 = -- * e 20
    10 * -- * d 10

    11 somaNumEsq0 retorne
    12 somaNumEsq1 retorne
    13 somaNumEsq2 retorne
    14 somaNumEsq3 retorne
    15 somaNumEsq4 retorne
    16 somaNumEsq5 retorne
    17 somaNumEsq6 retorne
    18 somaNumEsq7 retorne
    19 somaNumEsq8 retorne
    20 somaNumEsq9 retorne


fim

;blocos que somam com o menos significativo do operando da direita cujo número á esquerda é X
;no caso deste bloco aqui o numero vai somar da esquerda é 0, nos outros pode ser 1,2,3..
bloco somaNumEsq0 0

    ; 1 = setaResultEsq0Dir0
    ; 2 = setaResultEsq0Dir1
    ; 3 = setaResultEsq0Dir2
    ; 4 = setaResultEsq0Dir3
    ; 5 = setaResultEsq0Dir4
    ; 6 = setaResultEsq0Dir5
    ; 7 = setaResultEsq0Dir6
    ; 8 = setaResultEsq0Dir7
    ; 9 = setaResultEsq0Dir8
    ; 10 = setaResultEsq0Dir9

    0 + -- * e 1
    0 0 -- a d 1
    0 1 -- b d 2
    0 2 -- c d 3
    0 3 -- d d 4
    0 4 -- e d 5
    0 5 -- f d 6
    0 6 -- g d 7
    0 7 -- h d 8
    0 8 -- i d 9
    0 9 -- j d 10
    0 * -- * e 0

    1 setResEsq0Dir0 retorne
    2 setResEsq0Dir1 retorne
    3 setResEsq0Dir2 retorne
    4 setResEsq0Dir3 retorne
    5 setResEsq0Dir4 retorne
    6 setResEsq0Dir5 retorne
    7 setResEsq0Dir6 retorne
    8 setResEsq0Dir7 retorne
    9 setResEsq0Dir8 retorne
    10 setResEsq0Dir9 retorne

fim

bloco somaNumEsq1 0

    ; 1 = setaResultEsq1Dir0
    ; 2 = setaResultEsq1Dir1
    ; 3 = setaResultEsq1Dir2
    ; 4 = setaResultEsq1Dir3
    ; 5 = setaResultEsq1Dir4
    ; 6 = setaResultEsq1Dir5
    ; 7 = setaResultEsq1Dir6
    ; 8 = setaResultEsq1Dir7
    ; 9 = setaResultEsq1Dir8
    ; 10 = setaResultEsq1Dir9

    0 + -- * e 1
    0 0 -- a d 1
    0 1 -- b d 2
    0 2 -- c d 3
    0 3 -- d d 4
    0 4 -- e d 5
    0 5 -- f d 6
    0 6 -- g d 7
    0 7 -- h d 8
    0 8 -- i d 9
    0 9 -- j d 10
    0 * -- * e 0

    1 setResEsq1Dir0 retorne
    2 setResEsq1Dir1 retorne
    3 setResEsq1Dir2 retorne
    4 setResEsq1Dir3 retorne
    5 setResEsq1Dir4 retorne
    6 setResEsq1Dir5 retorne
    7 setResEsq1Dir6 retorne
    8 setResEsq1Dir7 retorne
    9 setResEsq1Dir8 retorne
    10 setResEsq1Dir9 retorne

fim

bloco somaNumEsq2 0

    ; 1 = setaResultEsq2Dir0
    ; 2 = setaResultEsq2Dir1
    ; 3 = setaResultEsq2Dir2
    ; 4 = setaResultEsq2Dir3
    ; 5 = setaResultEsq2Dir4
    ; 6 = setaResultEsq2Dir5
    ; 7 = setaResultEsq2Dir6
    ; 8 = setaResultEsq2Dir7
    ; 9 = setaResultEsq2Dir8
    ; 10 = setaResultEsq2Dir9

    0 + -- * e 1
    0 0 -- a d 1
    0 1 -- b d 2
    0 2 -- c d 3
    0 3 -- d d 4
    0 4 -- e d 5
    0 5 -- f d 6
    0 6 -- g d 7
    0 7 -- h d 8
    0 8 -- i d 9
    0 9 -- j d 10
    0 * -- * e 0

    1 setResEsq2Dir0 retorne
    2 setResEsq2Dir1 retorne
    3 setResEsq2Dir2 retorne
    4 setResEsq2Dir3 retorne
    5 setResEsq2Dir4 retorne
    6 setResEsq2Dir5 retorne
    7 setResEsq2Dir6 retorne
    8 setResEsq2Dir7 retorne
    9 setResEsq2Dir8 retorne
    10 setResEsq2Dir9 retorne

fim

bloco somaNumEsq3 0

    ; 1 = setaResultEsq3Dir0
    ; 2 = setaResultEsq3Dir1
    ; 3 = setaResultEsq3Dir2
    ; 4 = setaResultEsq3Dir3
    ; 5 = setaResultEsq3Dir4
    ; 6 = setaResultEsq3Dir5
    ; 7 = setaResultEsq3Dir6
    ; 8 = setaResultEsq3Dir7
    ; 9 = setaResultEsq3Dir8
    ; 10 = setaResultEsq3Dir9

    0 + -- * e 1
    0 0 -- a d 1
    0 1 -- b d 2
    0 2 -- c d 3
    0 3 -- d d 4
    0 4 -- e d 5
    0 5 -- f d 6
    0 6 -- g d 7
    0 7 -- h d 8
    0 8 -- i d 9
    0 9 -- j d 10
    0 * -- * e 0

    1 setResEsq3Dir0 retorne
    2 setResEsq3Dir1 retorne
    3 setResEsq3Dir2 retorne
    4 setResEsq3Dir3 retorne
    5 setResEsq3Dir4 retorne
    6 setResEsq3Dir5 retorne
    7 setResEsq3Dir6 retorne
    8 setResEsq3Dir7 retorne
    9 setResEsq3Dir8 retorne
    10 setResEsq3Dir9 retorne

fim

bloco somaNumEsq4 0

    ; 1 = setaResultEsq4Dir0
    ; 2 = setaResultEsq4Dir1
    ; 3 = setaResultEsq4Dir2
    ; 4 = setaResultEsq4Dir3
    ; 5 = setaResultEsq4Dir4
    ; 6 = setaResultEsq4Dir5
    ; 7 = setaResultEsq4Dir6
    ; 8 = setaResultEsq4Dir7
    ; 9 = setaResultEsq4Dir8
    ; 10 = setaResultEsq4Dir9

    0 + -- * e 1
    0 0 -- a d 1
    0 1 -- b d 2
    0 2 -- c d 3
    0 3 -- d d 4
    0 4 -- e d 5
    0 5 -- f d 6
    0 6 -- g d 7
    0 7 -- h d 8
    0 8 -- i d 9
    0 9 -- j d 10
    0 * -- * e 0

    1 setResEsq4Dir0 retorne
    2 setResEsq4Dir1 retorne
    3 setResEsq4Dir2 retorne
    4 setResEsq4Dir3 retorne
    5 setResEsq4Dir4 retorne
    6 setResEsq4Dir5 retorne
    7 setResEsq4Dir6 retorne
    8 setResEsq4Dir7 retorne
    9 setResEsq4Dir8 retorne
    10 setResEsq4Dir9 retorne

fim

bloco somaNumEsq5 0

    ; 1 = setaResultEsq5Dir0
    ; 2 = setaResultEsq5Dir1
    ; 3 = setaResultEsq5Dir2
    ; 4 = setaResultEsq5Dir3
    ; 5 = setaResultEsq5Dir4
    ; 6 = setaResultEsq5Dir5
    ; 7 = setaResultEsq5Dir6
    ; 8 = setaResultEsq5Dir7
    ; 9 = setaResultEsq5Dir8
    ; 10 = setaResultEsq5Dir9

    0 + -- * e 1
    0 0 -- a d 1
    0 1 -- b d 2
    0 2 -- c d 3
    0 3 -- d d 4
    0 4 -- e d 5
    0 5 -- f d 6
    0 6 -- g d 7
    0 7 -- h d 8
    0 8 -- i d 9
    0 9 -- j d 10
    0 * -- * e 0

    1 setResEsq5Dir0 retorne
    2 setResEsq5Dir1 retorne
    3 setResEsq5Dir2 retorne
    4 setResEsq5Dir3 retorne
    5 setResEsq5Dir4 retorne
    6 setResEsq5Dir5 retorne
    7 setResEsq5Dir6 retorne
    8 setResEsq5Dir7 retorne
    9 setResEsq5Dir8 retorne
    10 setResEsq5Dir9 retorne

fim

bloco somaNumEsq6 0

    ; 1 = setaResultEsq6Dir0
    ; 2 = setaResultEsq6Dir1
    ; 3 = setaResultEsq6Dir2
    ; 4 = setaResultEsq6Dir3
    ; 5 = setaResultEsq6Dir4
    ; 6 = setaResultEsq6Dir5
    ; 7 = setaResultEsq6Dir6
    ; 8 = setaResultEsq6Dir7
    ; 9 = setaResultEsq6Dir8
    ; 10 = setaResultEsq6Dir9

    0 + -- * e 1
    0 0 -- a d 1
    0 1 -- b d 2
    0 2 -- c d 3
    0 3 -- d d 4
    0 4 -- e d 5
    0 5 -- f d 6
    0 6 -- g d 7
    0 7 -- h d 8
    0 8 -- i d 9
    0 9 -- j d 10
    0 * -- * e 0

    1 setResEsq6Dir0 retorne
    2 setResEsq6Dir1 retorne
    3 setResEsq6Dir2 retorne
    4 setResEsq6Dir3 retorne
    5 setResEsq6Dir4 retorne
    6 setResEsq6Dir5 retorne
    7 setResEsq6Dir6 retorne
    8 setResEsq6Dir7 retorne
    9 setResEsq6Dir8 retorne
    10 setResEsq6Dir9 retorne

fim

bloco somaNumEsq7 0

    ; 1 = setaResultEsq7Dir0
    ; 2 = setaResultEsq7Dir1
    ; 3 = setaResultEsq7Dir2
    ; 4 = setaResultEsq7Dir3
    ; 5 = setaResultEsq7Dir4
    ; 6 = setaResultEsq7Dir5
    ; 7 = setaResultEsq7Dir6
    ; 8 = setaResultEsq7Dir7
    ; 9 = setaResultEsq7Dir8
    ; 10 = setaResultEsq7Dir9

    0 + -- * e 1
    0 0 -- a d 1
    0 1 -- b d 2
    0 2 -- c d 3
    0 3 -- d d 4
    0 4 -- e d 5
    0 5 -- f d 6
    0 6 -- g d 7
    0 7 -- h d 8
    0 8 -- i d 9
    0 9 -- j d 10
    0 * -- * e 0

    1 setResEsq7Dir0 retorne
    2 setResEsq7Dir1 retorne
    3 setResEsq7Dir2 retorne
    4 setResEsq7Dir3 retorne
    5 setResEsq7Dir4 retorne
    6 setResEsq7Dir5 retorne
    7 setResEsq7Dir6 retorne
    8 setResEsq7Dir7 retorne
    9 setResEsq7Dir8 retorne
    10 setResEsq7Dir9 retorne

fim

bloco somaNumEsq8 0

    ; 1 = setaResultEsq8Dir0
    ; 2 = setaResultEsq8Dir1
    ; 3 = setaResultEsq8Dir2
    ; 4 = setaResultEsq8Dir3
    ; 5 = setaResultEsq8Dir4
    ; 6 = setaResultEsq8Dir5
    ; 7 = setaResultEsq8Dir6
    ; 8 = setaResultEsq8Dir7
    ; 9 = setaResultEsq8Dir8
    ; 10 = setaResultEsq8Dir9

    0 + -- * e 1
    0 0 -- a d 1
    0 1 -- b d 2
    0 2 -- c d 3
    0 3 -- d d 4
    0 4 -- e d 5
    0 5 -- f d 6
    0 6 -- g d 7
    0 7 -- h d 8
    0 8 -- i d 9
    0 9 -- j d 10
    0 * -- * e 0

    1 setResEsq8Dir0 retorne
    2 setResEsq8Dir1 retorne
    3 setResEsq8Dir2 retorne
    4 setResEsq8Dir3 retorne
    5 setResEsq8Dir4 retorne
    6 setResEsq8Dir5 retorne
    7 setResEsq8Dir6 retorne
    8 setResEsq8Dir7 retorne
    9 setResEsq8Dir8 retorne
    10 setResEsq8Dir9 retorne

fim

bloco somaNumEsq9 0

    ; 1 = setaResultEsq9Dir0
    ; 2 = setaResultEsq9Dir1
    ; 3 = setaResultEsq9Dir2
    ; 4 = setaResultEsq9Dir3
    ; 5 = setaResultEsq9Dir4
    ; 6 = setaResultEsq9Dir5
    ; 7 = setaResultEsq9Dir6
    ; 8 = setaResultEsq9Dir7
    ; 9 = setaResultEsq9Dir8
    ; 10 = setaResultEsq9Dir9

    0 + -- * e 1
    0 0 -- a d 1
    0 1 -- b d 2
    0 2 -- c d 3
    0 3 -- d d 4
    0 4 -- e d 5
    0 5 -- f d 6
    0 6 -- g d 7
    0 7 -- h d 8
    0 8 -- i d 9
    0 9 -- j d 10
    0 * -- * e 0

    1 setResEsq9Dir0 retorne
    2 setResEsq9Dir1 retorne
    3 setResEsq9Dir2 retorne
    4 setResEsq9Dir3 retorne
    5 setResEsq9Dir4 retorne
    6 setResEsq9Dir5 retorne
    7 setResEsq9Dir6 retorne
    8 setResEsq9Dir7 retorne
    9 setResEsq9Dir8 retorne
    10 setResEsq9Dir9 retorne

fim

;Blocos que setam o resultado com 0 à esquerda
bloco setResEsq0Dir0 0
    0 _ -- 0 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq0Dir1 0
    0 _ -- 1 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq0Dir2 0
    0 _ -- 2 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq0Dir3 0
    0 _ -- 3 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq0Dir4 0
    0 _ -- 4 i 1
    0 * -- * d 0
    1 moverFimResult retorne

fim

bloco setResEsq0Dir5 0
    0 _ -- 5 i moverFimResult
    0 * -- * d 0
fim

bloco setResEsq0Dir6 0
    0 _ -- 6 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq0Dir7 0
    0 _ -- 7 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq0Dir8 0
    0 _ -- 8 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq0Dir9 0
    0 _ -- 9 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

;Blocos que setam o resultado com 1 à esquerda
bloco setResEsq1Dir0 0
    0 _ -- 1 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq1Dir1 0
    0 _ -- 2 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq1Dir2 0
    0 _ -- 3 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq1Dir3 0
    0 _ -- 4 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq1Dir4 0
    0 _ -- 5 i 1
    0 * -- * d 0
    1 moverFimResult retorne

fim

bloco setResEsq1Dir5 0
    0 _ -- 6 i moverFimResult
    0 * -- * d 0
fim

bloco setResEsq1Dir6 0
    0 _ -- 7 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq1Dir7 0
    0 _ -- 8 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq1Dir8 0
    0 _ -- 9 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

;carry
bloco setResEsq1Dir9 0
    0 = -- * d 0
    0 _ -- 0 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim


;Blocos que setam o resultado com 2 à esquerda
bloco setResEsq2Dir0 0
    0 _ -- 2 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq2Dir1 0
    0 _ -- 3 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq2Dir2 0
    0 _ -- 4 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq2Dir3 0
    0 _ -- 5 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq2Dir4 0
    0 _ -- 6 i 1
    0 * -- * d 0
    1 moverFimResult retorne

fim

bloco setResEsq2Dir5 0
    0 _ -- 7 i moverFimResult
    0 * -- * d 0
fim

bloco setResEsq2Dir6 0
    0 _ -- 8 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq2Dir7 0
    0 _ -- 9 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq2Dir8 0
    0 = -- * d 0
    0 _ -- 0 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq2Dir9 0
    0 = -- * d 0
    0 _ -- 1 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

;Blocos que setam o resultado com 3 à esquerda
bloco setResEsq3Dir0 0
    0 _ -- 3 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq3Dir1 0
    0 _ -- 4 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq3Dir2 0
    0 _ -- 5 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq3Dir3 0
    0 _ -- 6 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq3Dir4 0
    0 _ -- 7 i 1
    0 * -- * d 0
    1 moverFimResult retorne

fim

bloco setResEsq3Dir5 0
    0 _ -- 8 i moverFimResult
    0 * -- * d 0
fim

bloco setResEsq3Dir6 0
    0 _ -- 9 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq3Dir7 0
    0 = -- * d 0
    0 _ -- 0 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq3Dir8 0
    0 = -- * d 0
    0 _ -- 1 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq3Dir9 0
    0 = -- * d 0
    0 _ -- 2 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

;Blocos que setam o resultado com 4 à esquerda
bloco setResEsq4Dir0 0
    0 _ -- 0 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq4Dir1 0
    0 _ -- 5 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq4Dir2 0
    0 _ -- 6 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq4Dir3 0
    0 _ -- 7 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq4Dir4 0
    0 _ -- 8 i 1
    0 * -- * d 0
    1 moverFimResult retorne

fim

bloco setResEsq4Dir5 0
    0 _ -- 9 i moverFimResult
    0 * -- * d 0
fim

bloco setResEsq4Dir6 0
    0 = -- * d 0
    0 _ -- 0 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq4Dir7 0
    0 = -- * d 0
    0 _ -- 1 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq4Dir8 0
    0 = -- * d 0
    0 _ -- 2 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq4Dir9 0
    0 = -- * d 0
    0 _ -- 3 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

;Blocos que setam o resultado com 5 à esquerda
bloco setResEsq5Dir0 0
    0 _ -- 5 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq5Dir1 0
    0 _ -- 6 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq5Dir2 0
    0 _ -- 7 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq5Dir3 0
    0 _ -- 8 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq5Dir4 0
    0 _ -- 9 i 1
    0 * -- * d 0
    1 moverFimResult retorne

fim

bloco setResEsq5Dir5 0
    0 = -- * d 0
    0 _ -- 0 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq5Dir6 0
    0 = -- * d 0
    0 _ -- 1 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq5Dir7 0
    0 = -- * d 0
    0 _ -- 2 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq5Dir8 0
    0 = -- * d 0
    0 _ -- 3 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq5Dir9 0
    0 = -- * d 0
    0 _ -- 4 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

;Blocos que setam o resultado com 6 à esquerda
bloco setResEsq6Dir0 0
    0 _ -- 6 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq6Dir1 0
    0 _ -- 7 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq6Dir2 0
    0 _ -- 8 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq6Dir3 0
    0 _ -- 9 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq6Dir4 0
    0 = -- * d 0
    0 _ -- 0 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq6Dir5 0
    0 = -- * d 0
    0 _ -- 1 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq6Dir6 0
    0 = -- * d 0
    0 _ -- 2 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq6Dir7 0
    0 = -- * d 0
    0 _ -- 3 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq6Dir8 0
    0 = -- * d 0
    0 _ -- 4 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq6Dir9 0
    0 = -- * d 0
    0 _ -- 5 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim


;Blocos que setam o resultado com 7 à esquerda
bloco setResEsq7Dir0 0
    0 _ -- 7 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq7Dir1 0
    0 _ -- 8 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq7Dir2 0
    0 _ -- 9 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq7Dir3 0
    0 = -- * d 0
    0 _ -- 0 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq7Dir4 0
    0 = -- * d 0
    0 _ -- 1 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq7Dir5 0
    0 = -- * d 0
    0 _ -- 2 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq7Dir6 0
    0 = -- * d 0
    0 _ -- 3 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq7Dir7 0
    0 = -- * d 0
    0 _ -- 4 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq7Dir8 0
    0 = -- * d 0
    0 _ -- 5 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq7Dir9 0
    0 = -- * d 0
    0 _ -- 6 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

;Blocos que setam o resultado com 8 à esquerda
bloco setResEsq8Dir0 0
    0 _ -- 8 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq8Dir1 0
    0 _ -- 9 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq8Dir2 0
    0 = -- * d 0
    0 _ -- 0 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq8Dir3 0
    0 = -- * d 0
    0 _ -- 1 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq8Dir4 0
    0 = -- * d 0
    0 _ -- 2 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq8Dir5 0
    0 = -- * d 0
    0 _ -- 3 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq8Dir6 0
    0 = -- * d 0
    0 _ -- 4 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq8Dir7 0
    0 = -- * d 0
    0 _ -- 5 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq8Dir8 0
    0 = -- * d 0
    0 _ -- 6 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq8Dir9 0
    0 = -- * d 0
    0 _ -- 7 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

;Blocos que setam o resultado com 9 à esquerda
bloco setResEsq9Dir0 0
    0 _ -- 9 i 1
    0 * -- * d 0
    1 moverFimResult retorne
fim

bloco setResEsq9Dir1 0
    0 = -- * d 0
    0 _ -- 0 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq9Dir2 0
    0 = -- * d 0
    0 _ -- 1 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq9Dir3 0
    0 = -- * d 0
    0 _ -- 2 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq9Dir4 0
    0 = -- * d 0
    0 _ -- 3 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq9Dir5 0
    0 = -- * d 0
    0 _ -- 4 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq9Dir6 0
    0 = -- * d 0
    0 _ -- 5 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq9Dir7 0
    0 = -- * d 0
    0 _ -- 6 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq9Dir8 0
    0 = -- * d 0
    0 _ -- 7 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco setResEsq9Dir9 0
    0 = -- * d 0
    0 _ -- 8 e 1
    0 * -- * d 0
    1 soma1PrimeiroNum 2
    2 moverFimResult retorne
fim

bloco soma1PrimeiroNum 0

;0 = soma1noPrimeiroNum
;1 = soma1noPrimeiroNum2
;2 = primeiroElementoPosIgual

    0 + -- * e 1
    0 * -- * e 0
    1 0 -- k i 2
    1 1 -- l i 2
    1 2 -- m i 2
    1 3 -- n i 2
    1 4 -- o i 2
    1 5 -- p i 2
    1 6 -- q i 2
    1 7 -- r i 2
    1 8 -- s i 2
    1 9 -- t e 1
    1 _ -- u d 2
    1 * -- * e 1

    2 = -- * d retorne
    2 * -- * d 2

fim

;move resultado pro final deixando um espaço em braco após o '='
bloco moverFimResult 0

;0 = moverFimResult
;1 = movResult
;2 = movResultSeta0
;3 = movResultSeta1
;4 = movResultSeta2
;5 = movResultSeta3
;6 = movResultSeta4
;7 = movResultSeta5
;8 = movResultSeta6
;9 = movResultSeta7
;10 = movResultSeta8
;11 = movResultSeta9

    0 _ -- * e 1
    0 * -- * d 0

    1 = -- * i retorne

    1 a -- _ e 1
    1 b -- _ e 1
    1 c -- _ e 1
    1 d -- _ e 1
    1 e -- _ e 1
    1 f -- _ e 1
    1 g -- _ e 1
    1 h -- _ e 1
    1 i -- _ e 1
    1 j -- _ e 1

    ;verificando qual numero setar
    1 _ -- * e 1
    1 0 -- _ d 2
    1 1 -- _ d 3
    1 2 -- _ d 4
    1 3 -- _ d 5
    1 4 -- _ d 6
    1 5 -- _ d 7
    1 6 -- _ d 8
    1 7 -- _ d 9
    1 8 -- _ d 10
    1 9 -- _ d 11

    2 _ -- 0 e 1
    3 _ -- 1 e 1
    4 _ -- 2 e 1
    5 _ -- 3 e 1
    6 _ -- 4 e 1
    7 _ -- 5 e 1
    8 _ -- 6 e 1
    9 _ -- 7 e 1
    10 _ -- 8 e 1
    11 _ -- 9 e 1

fim

bloco resPronto 0

;1 = resultadoPronto
;2 = resultadoProntoSeta0
;3 = resultadoProntoSeta1
;4 = resultadoProntoSeta2
;5 = resultadoProntoSeta3
;6 = resultadoProntoSeta4
;7 = resultadoProntoSeta5
;8 = resultadoProntoSeta6
;9 = resultadoProntoSeta7
;10 = resultadoProntoSeta8
;11 = resultadoProntoSeta9
    ;volta os algarismos no lugar das letras
    0 a -- 0 d 0
    0 b -- 1 d 0
    0 c -- 2 d 0
    0 d -- 3 d 0
    0 e -- 4 d 0
    0 f -- 5 d 0
    0 g -- 6 d 0
    0 h -- 7 d 0
    0 i -- 8 d 0
    0 j -- 9 d 0

    0 = -- * d 0
    0 + -- * d 0
    0 _ -- * d 1

    ;resultadoPronto
    1 0 -- * e 2
    1 1 -- * e 3
    1 2 -- * e 4
    1 3 -- * e 5
    1 4 -- * e 6
    1 5 -- * e 7
    1 6 -- * e 8
    1 7 -- * e 9
    1 8 -- * e 10
    1 9 -- * e 11
    1 _ -- * i retorne

    2 _ -- 0 d 2
    2 * -- _ d 1

    3 _ -- 1 d 3
    3 * -- _ d 1

    4 _ -- 2 d 4
    4 * -- _ d 1

    5 _ -- 3 d 5
    5 * -- _ d 1

    6 _ -- 4 d 6
    6 * -- _ d 1

    7 _ -- 5 d 7
    7 * -- _ d 1

    8 _ -- 6 d 8
    8 * -- _ d 1

    9 _ -- 7 d 9
    9 * -- _ d 1

    10 _ -- 8 d 10
    10 * -- _ d 1

    11 _ -- 9 d 11
    11 * -- _ d 1

fim

