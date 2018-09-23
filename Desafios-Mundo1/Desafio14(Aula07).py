#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.
Tc = float(input('Digite a temperatura em ºC:'))
Tf = (Tc/5) * 9 + 32
print('A temperatura {0}ºC convertida para ºF é: {1:.2f}ºF'.format(Tc, Tf))