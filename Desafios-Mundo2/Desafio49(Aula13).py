# Faça uma tabuada de um número escolhido pelo usuário, utilizando um laço for.
n = int(input('Informe um número para gerar a sua tabuada: '))
print('='*12, 'Tabuada de {}'.format(n), 12*'=')
for t in range(11):
    print('{0} * {1} = {2}'.format(n, t, n*t))
print('=' * 12, 'Tabuada de {}'.format(n), 12 * '=')
