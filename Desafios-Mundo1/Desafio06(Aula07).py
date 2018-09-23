#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math

n = int(input('Digite um número: '))
#Dobro do número
dobro = n*2
#Triplo do número
triplo = n*3
#Raiz quadrada do número
raiz = math.sqrt(n) #Ou n**(1/2)
print('Dobro de {0} = {1}\nTriplo de {0} = {2}\nRaiz quadrada de {0} = {3}'.format(n, dobro, triplo, raiz))
