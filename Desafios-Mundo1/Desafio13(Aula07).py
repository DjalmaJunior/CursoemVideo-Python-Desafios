#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o salário:'))
salarioC = salario + (salario*0.15)#Salário Corrigido com 15% de aumento
print('O salário de R${0:.2f}, com 15% de aumento, fica no valor de R${1:.2f}.'.format(salario, salarioC))

