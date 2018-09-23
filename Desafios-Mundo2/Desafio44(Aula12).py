# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# 1. À vista dinheiro/cheque: 10% de desconto
# 2. À vista no cartão: 5% de desconto
# 3. Em até 2x no cartão: preço normal
# 4. 3x ou mais no cartão: 20% de juros
precoN = float(input('Informe o valor do produto: R$'))  # Preço normal
while True:
    try:
        condicaoP = int(input('\n\nInforme a condição de pagamento:\n\nPOR FAVOR, DIGITE APENAS O NÚMERO DA OPÇÃO!!\n\n1. À vista dinheiro/cheque: 10% de desconto\n2. À vista no cartão: 5% de desconto\n3. Em até 2x no cartão: preço normal\n4. 3x ou mais no cartão: 20% de juros\n\n'))  # Condição de pagamento
        if condicaoP != 1 and condicaoP != 2 and condicaoP != 3 and condicaoP != 4:
            print('\033[1;31mSão válidos apenas os números diponíveis na lista de opções!\033[m')
        else:
            break
    except ValueError:
        print('\033[1;31mSão válidos apenas os números diponíveis na lista de opções!\033[m')
if condicaoP == 1:
    descricao = 'À vista dinheiro/cheque: 10% de desconto'  # Descrição da opção escolhida
    precoC = precoN - (precoN * 0.1)  # Preço corrigido
elif condicaoP == 2:
    descricao = 'À vista no cartão: 5% de desconto'  # Descrição da opção escolhida
    precoC = precoN - (precoN * 0.05)  # Preço corrigido
elif condicaoP == 3:
    descricao = 'Em até 2x no cartão: preço normal'  # Descrição da opção escolhida
    precoC = precoN  # Preço corrigido
else:
    descricao = '3x ou mais no cartão: 20% de juros'  # Descrição da opção escolhida
    precoC = precoN + (precoN * 0.2)  # Preço corrigido
print('Valor normal do produto: R${0:.2f}\nOpção de pagamento: {1}\nValor a ser pago: {2:.2f}'.format(precoN, descricao, precoC))
