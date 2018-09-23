# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a  média atingida:
# 1. Média abaixo de 5.0: REPROVADO!
# 2. Média entre 5.0 e 6.9: RECUPERAÇÃO!
# 3. Média 7.0 ou superior: APROVADO!
nota = []
for i in range(2):
    nota.append(float(input('Digite a {0}ª nota: '.format(i+1))))
if (nota[0]+nota[1])/2 < 5:
    print('Primeira nota: {0:.1f}\nSegunda nota: {1:.1f}'.format(nota[0], nota[1]))
    print('Media: {0:.1f}\nREPROVADO!'.format((nota[0]+nota[1])/2))
elif 5 <= (nota[0]+nota[1])/2 <= 6.9:
    print('Primeira nota: {0:.1f}\nSegunda nota: {1:.1f}'.format(nota[0], nota[1]))
    print('Media: {0:.1f}\nRECUPERAÇÃO!'.format((nota[0] + nota[1]) / 2))
else:
    print('Primeira nota: {0:.1f}\nSegunda nota: {1:.1f}'.format(nota[0], nota[1]))
    print('Media: {0:.1f}\nAPROVADO!'.format((nota[0] + nota[1]) / 2))
