# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# 1. Até 9 anos: MIRIM
# 2. Até 14 anos: INFANTIL
# 3. Até 19 anos: JUNIOR
# 4. Até 20 anos: SÊNIOR
# 5. Acima: MASTER
from datetime import datetime
nasc = int(input('Digite o ano de nascimento do atleta: '))
if datetime.now().year - nasc <= 9:
    if datetime.now().year - nasc == 1:
        print('Idade do atleta: {0} ano\nClassificação: MIRIM'.format(datetime.now().year - nasc))
    else:
        print('Idade do atleta: {0} anos\nClassificação: MIRIM'.format(datetime.now().year - nasc))
elif 9 < datetime.now().year - nasc <= 14:
    print('Idade do atleta: {0} anos\nClassificação: INFANTIL'.format(datetime.now().year - nasc))
elif 14 < datetime.now().year - nasc <= 19:
    print('Idade do atleta: {0} anos\nClassificação: JUNIOR'.format(datetime.now().year - nasc))
elif 19 < datetime.now().year - nasc <= 20:
    print('Idade do atleta: {0} anos\nClassificação: SÊNIOR'.format(datetime.now().year - nasc))
else:
    print('Idade do atleta: {0} anos\nClassificação: MASTER'.format(datetime.now().year - nasc))
