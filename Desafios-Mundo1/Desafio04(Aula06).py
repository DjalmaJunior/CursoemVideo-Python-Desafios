#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
entrada = input('Digite algum valor: ')
if entrada.isalpha():
    print('{0} é do tipo String'.format(entrada))
elif entrada.isnumeric():
    print('{0} é do tipo Numérico'.format(entrada))
elif entrada.isalnum():
    print('{0} é do tipo Alfanumérico'.format(entrada))


