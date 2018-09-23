#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, tan, cos, radians
angulo = float(input('Digite o ângulo:'))
print('Ângulo informado: {0}º\nSeno do ângulo({0}): {1:.2f}\nCosseno do ângulo({0}): {2:.2f}\nTangente do ângulo({0}): {3:.2f}'.format(angulo, sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))
