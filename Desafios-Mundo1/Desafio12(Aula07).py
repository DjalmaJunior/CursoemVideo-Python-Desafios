#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
valor = float(input('Digite o preço do produto:'))
valorC = valor - (valor*0.05)
print('O produto que custa R${0:.2f}, corrigido com o desconto de 5%, fica no preço de R${1:.2f}'.format(valor, valorC))
