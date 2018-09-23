# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lido.
p = []
for i in range(5):
    p.append(float(input('Digite o peso da {}ª pessoa: '.format(i+1))))
p.sort()
print('O menor peso lido foi: {0:.2f}kg\nO maior peso lido foi: {1:.2f}kg'.format(p[0], p[len(p)-1]))
