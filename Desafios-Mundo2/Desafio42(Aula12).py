# Refaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
# 1. Equilátero: todos os lados iguais
# 2. Isósceles: dois lados iguais
# 3. Escaleno: todos os lados diferentes
c = []  # Comprimentos das retas
for i in range(3):
    c.append(float(input('Informe o comprimento da {0}ª reta: '.format(i+1))))
if c[0] == c[1] == c[2]:
    tipo = 'Tipo Equilátero: todos os lados iguais.'
elif c[0] == c[1] != c[2] or c[1] == c[2] != c[0] or c[0] == c[2] != c[1]:
    tipo = 'Tipo Isósceles: dois lados iguais.'
elif c[0] != c[1] != c[2]:
    tipo = 'Tipo Escaleno: todos os lados diferentes.'
if abs(c[1]-c[2]) < c[0] < c[1]+c[2] and abs(c[0]-c[2]) < c[1] < c[0]+c[2] and abs(c[0]-c[1]) < c[2] < c[0]+c[1]:
    print('As retas {0}, {1} e {2} podem formar um triângulo. {3}'.format(c[0], c[1], c[2], tipo))
else:
    print('As retas {0}, {1} e {2} não podem formar um triângulo.'.format(c[0], c[1], c[2]))
