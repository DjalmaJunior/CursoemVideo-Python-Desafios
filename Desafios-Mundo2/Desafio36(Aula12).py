# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e
# em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
print("\33[1;33;44m-=-" * 17 + "=-\33[m" + """
\33[1;33;44m-=-Programa de avaliação bancária para empréstimos-=-\33[m
""" + "\33[1;33;44m-=-" * 17 + "=-\33[m")
vcasa = float(input('Informe o valor da casa: R$'))  # Valor da casa.
salario = float(input('Informe o salário do comprador: R$'))
tempo = float(input('Informe em quantos anos a dívida será paga: '))
prestm = vcasa/(tempo*12) # Valor da casa dividido pelo número de meses de acordo com o valor anual = Valor das prestações mensais.
if prestm > salario*0.3: # Se o valor das prestações mensais for maior que 30% do salário, o empréstimo é negado.
    print("\33[1;31mEmpréstimo negado!!\33[m\nMotivo: Valor das parcelas acima do salário informado...")
else:
    print("\33[1;33;44mEmpréstimo permitido!!\33[m\nInformações sobre o processo:\nValor da casa: R${0:.2f}\nSalário do comprador: R${1:.2f}\nTempo escolhido para pagamento da dívida: {2} anos\nValor das parcelas mensais: R${3:.2f}".format(vcasa, salario, tempo, prestm))
