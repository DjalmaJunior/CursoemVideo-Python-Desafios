#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
v = float(input('Informe a velocidade do carro:'))
multa = (v - 80) * 7
if multa > 0:
    print('Você excedeu a velocidade permitida(80Km/h)!\nMulta referente a infração cometida: R${0:.2f}\nValor por Km/h excedidos: R$7,00\nKm/h excedidos: {1}Km/h'.format(multa, v-80))
else:
    print('Não há multas para você! Parabéns, continue assim!')
