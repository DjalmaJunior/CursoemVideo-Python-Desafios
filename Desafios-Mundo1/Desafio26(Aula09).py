#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a ultima vez.
frase = input('Digite uma frase:').strip()
quant = frase.lower().count('a')
pi = frase.lower().find('a') #Posição Inicial
pf = frase.lower().rfind('a')#Posição Final
print("""Quantidade de vezes que a letra A aparece: {0}
Posição que a letra A aparece pela primeira vez: {1}
Posição que a letra A aparece pela ultima vez: {2}""".format(quant, pi, pf))