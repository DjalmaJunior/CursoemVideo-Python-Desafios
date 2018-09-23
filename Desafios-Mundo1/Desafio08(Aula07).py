#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Digite um número:'))
c = m*100
mm = m*1000
print('{0} metros em:\ncentímetros: {1:.0f}cm;\nMilímetros: {2:.0f}mm.'.format(m, c, mm))
