# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade(21 anos) e quantas já são maiores.
from datetime import datetime
idades = []  # Guarda as idades
quantM = 0  # Guarda quantos são maiores de idade
quantm = 0  # Guarda quantos são menores de idade
for i in range(7):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i + 1)))
    idades.append(datetime.now().year - ano)
for c in idades:
    if c >= 21:
        quantM += 1
    else:
        quantm += 1
print('Número de pessoas maiores de idade: {0} pessoas\nNúmero de pessoas menores de idade: {1} pessoas'.format(quantM, quantm))
