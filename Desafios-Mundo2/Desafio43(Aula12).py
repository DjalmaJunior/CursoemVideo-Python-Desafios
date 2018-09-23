# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a  tabela abaixo:
# 1. Abaixo de 18.5: Abaixo do peso!
# 2. Entre 18.5 e 25: Peso ideal!
# 3. 25 até 30: Sobrepeso!
# 4. 30 até 40: Obesidade!
# 5. Acima de 40: Obesidade mórbida!
altura = float(input('Digite a altura(em metros): '))
peso = float(input('Digite o peso(em quilogramas): '))
IMC = peso/altura**2
if IMC < 18.5:
    print('Abaixo do peso! IMC: {0:.2f}'.format(IMC))
elif 18.5 <= IMC <= 25:
    print('Peso ideal!IMC: {0:.2f}'.format(IMC))
elif 25 <= IMC <= 30:
    print('Sobrepeso!IMC: {0:.2f}'.format(IMC))
elif 30 <= IMC <= 40:
    print('Obesidade!IMC: {0:.2f}'.format(IMC))
else:
    print('Obesidade mórbida!IMC: {0:.2f}'.format(IMC))
