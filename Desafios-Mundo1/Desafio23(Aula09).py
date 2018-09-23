#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
#Ex: Digite um numero: 1834
#Unidade:4
#dezena:3
#centena:8
#milhar:1
n = int(input('Digite um número:'))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print("""Unidade: {0}
Dezena: {1}
Centena: {2}
Milhar: {3}""".format(u, d, c, m))