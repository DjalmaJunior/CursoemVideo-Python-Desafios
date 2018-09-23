# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.
print('\033[1;31mAtenção!! Não utilize traços ou quaisquer caracteres especiais.\033[m')
frase = str(input('Digite uma frase: ')).lower().strip()
c = 0  # Contador de letras iguais
aux = 0  # Contador auxiliar
frasel = []  # Armazena a frase em espaços
# Inserção da string na lista
for i in frase.replace(' ', ''):
    frasel.append(str(i))
# Preparando a lista para ser lida de trás para frente
frasel.reverse()
# Conferindo se os caracteres da lista revertida são os mesmos da string passada
for i in frase.replace(' ', ''):
    if i == frasel[aux]:
        c += 1
    aux += 1
# Se tem o mesmo número de letras corretas, imprime a mensagem
# "A frase x é um palíndromo", se não, imprime "A frase x não é um palíndromo".
if c == frase.replace(' ', '').__len__():
    print('A frase "{}" é um palíndromo'.format(frase.capitalize()))
else:
    print('A frase "{}" não é um palíndromo'.format(frase.capitalize()))
