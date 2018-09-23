# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
from itertools import repeat
from random import randint
while True:
    nr = randint(0, 5)  # Número inteiro aleatório
    n = int(input('Tente adivinhar qual o número, entre 0 e 5,  escolhido pelo computador: '))
    if nr == n:
        print("""PARABÉNS!! Você escolheu o mesmo número que o computador!
        Números escolhidos: Computador: {0}
                            Usuário: {1}""".format(nr, n))
        break
    else:
        print("""Que pena... você errou!!
        Números escolhidos: Computador: {0}
                            Usuário: {1}""".format(nr, n))
        resp = input('Quer tentar outra vez? y -> sim | n -> não')
        while resp != 'y' and resp != 'n':
            print('Somente y ou n como resposta!')
            resp = input('Quer tentar outra vez? y -> sim | n -> não')
        if resp == 'y':
            continue
        elif resp == 'n':
            print('Programa finalizado! Obrigado por usa-lo!')
            break
