#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
l = float(input('Digite a largura da parede em metros:'))
a = float(input('Digite a altura da parede em metros:'))
L = 2 #1 litro de tinta a cada 2m²
qt = (l*a)/L #Quantidade total de tinta
print('Para pintar uma parede de {0}m² serão utilizados {1}L de tinta.'.format(l*a, qt))
