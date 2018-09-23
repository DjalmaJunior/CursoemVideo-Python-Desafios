#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
print('{:=^50}'.format('Tabuada de um numero só'))
n = int(input('Digite um número:'))
for i in range(0,11):
    if(i<10):
        print('{0} * {1:2} = {2:2}\n'.format(n, i, n*i))
    else:
        print('{0} * {1:2} = {2:2}'.format(n, i, n * i))
print('{:=^50}'.format('Obrigado por usar o programa'))

