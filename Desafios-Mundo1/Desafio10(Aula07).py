#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
money = float(input('Quanto dinheiro você tem na carteira:'))
dolar = 3.27 #Reais
compra = money/dolar
resto = money % dolar
if compra < 1:
    print('Você não tem dinheiro suficiente para comprar dólar!')
elif(compra == 1):
    print('Você pode comprar {0} dólar.'.format(compra))
else:
    print('Você pode comprar {0:.2f} dólares e sobram {1:.2f} reais.'.format(compra, resto))
