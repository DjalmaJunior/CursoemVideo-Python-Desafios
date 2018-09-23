#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou Impar.
n = int(input('Digite um numero: '))
if n % 2 == 0:
    print('O número {0} é PAR!'.format(n))
else:
    print('O número {0} é IMPAR!'.format(n))
