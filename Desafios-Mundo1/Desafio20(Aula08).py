#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import choice
In = []
a = 0
for i in range(1, 5):
    In.append(input('Digite o nome do {0}º aluno: '.format(i)))
while a<4:
    a += 1
    s = choice(In)
    print('O {0}º aluno selecionado para apresentar é: {1}!!'.format(a, s))
    In.remove(s)