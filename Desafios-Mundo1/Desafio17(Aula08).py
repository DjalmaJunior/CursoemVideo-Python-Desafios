#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))
print('Valor dado para o Cateto Oposto:{}\nValor dado para o Cateto Adjacente:{}\nO valor da hipotenusa é {:.2f}'.format(co, ca, hypot(co, ca)))
