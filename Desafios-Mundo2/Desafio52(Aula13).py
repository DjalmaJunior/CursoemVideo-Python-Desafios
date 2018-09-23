# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
while True:
    try:
        print('Digite qualquer letra para parar o programa')
        n = int(input('Digite um número inteiro: '))
        for i in range(2, 10):
            if i != n:
                if n % i != 0:
                    r = '\033[1;31m{0} é número primo.\033[m'.format(n)  # Resultado
                else:
                    r = '\033[1;31m{0} não é número primo.\033[m'.format(n)  # Resultado
                    break
        print(r+'\n')
    except Exception:
        print('\033[4;36mPrograma encerrado\033[m')
        break
