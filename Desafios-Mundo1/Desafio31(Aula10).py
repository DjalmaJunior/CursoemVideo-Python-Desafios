# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
while True:
    dist = float(input('Informe a distância, em Km, da viagem desejada: '))
    if 0 < dist <= 200:
        valor = 0.5 * dist
        print('O valor cobrado pela viagem é: R${0:.2f}'.format(valor))
        break
    elif dist > 200:
        valor = 0.45 * dist
        print('O valor cobrado pela viagem é: R${0:.2f}'.format(valor))
        break
    else:
        print('Informe uma distância válida!')
        continue
