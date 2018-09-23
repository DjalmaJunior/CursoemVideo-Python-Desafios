# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois e maior que o valor absoluto da diferença entre essas medidas.
c = []  # Comprimentos das retas
for i in range(0, 3):
    c.append(float(input('Informe o comprimento da {0}ª reta: '.format(i+1))))
if abs(c[1]-c[2]) < c[0] < c[1]+c[2] and abs(c[0]-c[2]) < c[1] < c[0]+c[2] and abs(c[0]-c[1]) < c[2] < c[0]+c[1]:
    print('As retas {0}, {1} e {2} podem formar um triângulo.'.format(c[0], c[1], c[2]))
else:
    print('As retas {0}, {1} e {2} não podem formar um triângulo.'.format(c[0], c[1], c[2]))
