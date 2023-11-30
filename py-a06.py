## a) Explique o que o código faz:
## O código utiliza o módulo random em Python para selecionar aleatoriamente um elemento da lista lista. 
## A função random.choice(lista) escolhe um elemento aleatório da lista e o atribui à variável x. 
## Portanto, após a execução desse trecho de código, x conterá um valor aleatório entre 1 e 5 (inclusive), 
## já que a lista é [1, 2, 3, 4, 5].

## b) Trecho de código para gerar um número inteiro aleatório entre 10 e 20 (inclusive):

import random

numero_aleatorio = random.randint(10, 20)
print(numero_aleatorio)


## c) Trecho de código para gerar uma lista com 5 elementos inteiros aleatórios entre 1 e 100 (inclusive): 

import random

lista_aleatoria = [random.randint(1, 100) for _ in range(5)]
print(lista_aleatoria)
