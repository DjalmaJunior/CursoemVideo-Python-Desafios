# Faça um programa que mostre na tela uma contagem
# regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
for c in range(10, 0, -1):
    print(c)
    sleep(1)
cf = 31  # Cor da fonte
for i in range(42, 46):
    print('\033[1;{0};{1}mBOOOM\033[m'.format(cf, i))
    cf += 1
