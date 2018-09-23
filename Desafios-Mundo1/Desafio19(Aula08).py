#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
In = []
for i in range(1, 5):
    In.append(input('Digite o nome do {0}º aluno:'.format(i)))
print('O aluno escolhido para apagar o quadro foi -> {}'.format(choice(In)))
