#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
n = input('Digite um nome:')
b = bool
if n == 'silva'.upper() or n == 'silva' or n == 'silva'.capitalize():
    print('O nome {0} tem "Silva"'.format(n))
else:
    for i in range(0, len(n.split())):
        if n.split()[i] == 'silva'.upper() or n.split()[i] == 'silva' or n.split()[i] == 'silva'.capitalize():
            print('O nome {0} tem "Silva"'.format(n))
            b = True
            break
        else:
            b = False
            continue
    if b == False:
        print('O nome {0} não possui "Silva"'.format(n))