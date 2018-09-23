# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior;
# O segundo valor é maior;
# Os dois valores são iguais.
n = []
for i in range(2):
    n.append(int(input('Digite o {0}º número: '.format(i+1))))
if n[0] > n[1]:
    print('O primeiro número é maior ({0} > {1})'.format(n[0], n[1]))
elif n[0] < n[1]:
    print('O segundo número é maior ({0} < {1})'.format(n[0], n[1]))
else:
    print('Os dois valores são iguais ({0} = {1})'.format(n[0], n[1]))
