#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = int(input('Digite a primeira nota:'))
n2 = int(input('Digite a segunda nota:'))
media = (n1+n2)/2
print('A média das notas {0} e {1} é {2}'.format(n1, n2, media))
