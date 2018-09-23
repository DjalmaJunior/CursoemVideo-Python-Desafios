# Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
while True:
    try:
        n = []  # Lista para guardar os números fornecidos pela entrada
        s = 0  # Variavel para guardar a soma dos numeros pares
        p = []  # Lista para guardar os números pares
        print('Digite 6 números inteiros')
        for i in range(6):
            n.append(int(input('Digite o {}º número: '.format(i+1))))
        for c in n:
            if c % 2 == 0:
                s += c
                p.append(c)
        print('Resultado da soma dos números pares é: {0}'.format(s), '\nNúmeros fornecidos: {0}\nNúmeros pares utilizados na soma: '.format(n), end='')
        p.sort()  # Colocando os números em ordem crescente
        for i in p:
            if i != p[len(p)-1] and i != p[len(p)-2]:
                print(i, end=', ')
            elif i == p[len(p)-2]:
                print(i, end=' e ')
            else:
                print('{}.'.format(i))
        break
    except Exception:
        print('\n'+40*'='+'Somente números inteiros!!'+40*'='+'\n')
