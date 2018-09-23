#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.
s = float(input('Informe o salário: '))#Salário
if s > 1250:
    a = 10  # Aumento
    ns = s + (s*(a/100)) #Novo salário
elif s <= 1250:
    a = 15#Aumento
    ns = s + (s*(a/100)) #Novo salário
print('O teu salário de R${0:.2f} corrigido com {1}% de aumento é: R${2:.2f}'.format(s, a, ns))
