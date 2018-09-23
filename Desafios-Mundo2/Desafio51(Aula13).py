# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
n = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))
for c in range(10):
    if c == 0:
        print(n, end=' ')
    elif c != 9:
        n += r
        print(n, end=' ')
    else:
        n += r
        print(n)
