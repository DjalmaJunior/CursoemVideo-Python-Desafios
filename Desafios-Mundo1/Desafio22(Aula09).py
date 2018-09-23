#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras ao todo(sem considerar espaços).
#Quantas letras tem o primeiro nome.
nome = input('Digite o teu nome:')
M = nome.upper()
m = nome.lower()
quant = len(nome.replace(" ", ""))
quantP = len(nome.split()[0])
print("""Nome com todas as letras maiúsculas:{0}
Nome com todas as letras minúsculas:{1}
Número de letras ao todo no nome:{2}
Número de letras que tem o primeiro nome:{3}""".format(M, m, quant, quantP))
print('Djalma Junior')