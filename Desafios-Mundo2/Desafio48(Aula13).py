# Faça um programa que calcule a soma entre todos os
# números ímpares que são múltiplos de três e que se
# encontram no intervalo de 1 até 500.
s = 0
for n in range(1, 501):
    if n % 2 != 0 and n % 3 == 0:
        s += n
print('Soma dos números ímpares e múltiplos de 3: {}'.format(s))