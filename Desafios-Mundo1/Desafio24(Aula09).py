#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".
n = input('Digite o nome de uma cidade:')
if n.split()[0] == 'Santos'.upper() or n.split()[0] == 'santos' or n.split()[0] == 'santos'.capitalize() or n == 'santos'.upper() or n == 'santos' or n == 'santos'.capitalize():
    print('O nome "{0}" começa com "Santos"'.format(n))
else:
    print('O nome "{0} não começa com "Santos"'.format(n))