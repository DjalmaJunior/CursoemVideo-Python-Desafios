#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
from datetime import date
ano = int(input('Digite um ano(Digite 0 para selecionar o ano atual): '))
if ano == 0:
    ano = date.today().year

#As 3 condições para um determinado ano ser bissexto são:

#1. O ano é divisível por quatro, sem deixar resto;
#2. Se o ano for divisível por 100 (anos terminados em dois zeros), não é bissexto, exceto se;
#3. Ele também for divisível por 400 (nesse caso ele será bissexto).

if ano % 4 != 0 or ano % 100 == 0 and ano % 400 != 0:
    print('O ano {0} não é bissexto!'.format(ano))
else:
    print('O ano {0} é bissexto!'.format(ano))
