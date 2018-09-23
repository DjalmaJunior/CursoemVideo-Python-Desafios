# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n = []
for i in range(0, 3):
    n.append(float(input('Digite {0}º número:'.format(i + 1))))
maior = n[0]
menor = n[0]
for i in n:
    for j in range(0, len(n)):
        if i > n[j] and i > maior:
            maior = i
        elif i == n[j]:
            ''
        elif i < n[j] and i < menor:
            menor = i
print('O maior número é {0} e o menor é o {1}'.format(maior, menor))
