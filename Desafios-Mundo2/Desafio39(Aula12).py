# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# 1. Se ele ainda vai ser alistar ao serviço militar.
# 2. Se é a hora de se alistar.
# 3. Se já passou do tempo do alistamento.
from datetime import datetime
nasc = int(input('Informe o ano de nascimento: '))
idadeMilitar = datetime.now().year - 18
print('=========='*5 + ' ***** ', datetime.now().day, '/', datetime.now().month, '/', datetime.now().year, ' ***** ' + '=========='*5)
if idadeMilitar < nasc:
    if nasc - idadeMilitar == 1:
        print('Ainda irá se alistar ao serviço militar(falta {0} ano para se alistar).\nAno de alistamento: {1}'.format(nasc - idadeMilitar, datetime.now().year-(idadeMilitar - nasc)))
    else:
        print('Ainda irá se alistar ao serviço militar(faltam {0} anos para se alistar).\nAno de alistamento: {1}'.format(nasc - idadeMilitar, datetime.now().year-(idadeMilitar - nasc)))
elif idadeMilitar == nasc:
    print('É hora de se alistar ao serviço militar, jovem!')
else:
    if idadeMilitar - nasc == 1:
        print('Já passou o tempo de alistamento para você(teu tempo de alistamento foi há {0} ano)!\nAno de alistamento: {1}'.format(idadeMilitar - nasc, datetime.now().year-(idadeMilitar - nasc)))
    else:
        print('Já passou o tempo de alistamento para você(teu tempo de alistamento foi há {0} anos)!\nAno de alistamento: {1}'.format(idadeMilitar - nasc, datetime.now().year-(idadeMilitar - nasc)))
print('=========='*5 + ' ***** ', datetime.now().day, '/', datetime.now().month, '/', datetime.now().year, ' ***** ' + '=========='*5)
