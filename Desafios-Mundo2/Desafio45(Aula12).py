# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep

opcoes = ['pedra', 'papel', 'tesoura']
opcaoPC = randint(0, 2)  # Opção escolhida pelo computador
nr = int(input('Digite o número de rodadas desejado para o jogo: '))  # Numero de rodadas
for i in range(nr):
    while True:
        try:
            print('\nRODADA Nº{0}'.format(i+1))
            opcaoj = int(input('Escolha a tua jogada: 1-Pedra 2-Papel 3-Tesoura 4-Encerrar\n\n')) - 1  # Opção do jogador
            if opcaoj + 1 != 1 and opcaoj + 1 != 2 and opcaoj + 1 != 3 and opcaoj + 1 != 4:
                print('Escolha apenas um número das opções disponíveis!')
            elif opcaoj + 1 == 4:
                exit()
            else:
                break
        except ValueError:
            print('Apenas NÚMEROS são permitidos!!')
    print('Computador escolhendo...')
    sleep(5)  # Faz o computador "dormir" por 5 segundos
    if opcoes[opcaoPC] == 'pedra' and opcoes[opcaoj] == 'tesoura':
        print('\nO computador venceu!!\nVocê escolheu: {0}\nO computador escolheu: {1}\n\n'.format(opcoes[opcaoj], opcoes[opcaoPC]))
    elif opcoes[opcaoPC] == 'papel' and opcoes[opcaoj] == 'pedra':
        print('\nO computador venceu!!\nVocê escolheu: {0}\nO computador escolheu: {1}\n\n'.format(opcoes[opcaoj], opcoes[opcaoPC]))
    elif opcoes[opcaoPC] == 'tesoura' and opcoes[opcaoj] == 'papel':
        print('\nO computador venceu!!\nVocê escolheu: {0}\nO computador escolheu: {1}\n\n'.format(opcoes[opcaoj], opcoes[opcaoPC]))
    elif opcoes[opcaoPC] == 'pedra' and opcoes[opcaoj] == 'papel':
        print('\nVocê venceu!!\nVocê escolheu: {0}\nO computador escolheu: {1}\n\n'.format(opcoes[opcaoj], opcoes[opcaoPC]))
    elif opcoes[opcaoPC] == 'papel' and opcoes[opcaoj] == 'tesoura':
        print('\nVocê venceu!!\nVocê escolheu: {0}\nO computador escolheu: {1}\n\n'.format(opcoes[opcaoj], opcoes[opcaoPC]))
    elif opcoes[opcaoPC] == 'tesoura' and opcoes[opcaoj] == 'pedra':
        print('\nVocê venceu!!\nVocê escolheu: {0}\nO computador escolheu: {1}\n\n'.format(opcoes[opcaoj], opcoes[opcaoPC]))
    else:
        print('\nEmpate!!\nVocê escolheu: {0}\nO computador escolheu: {1}\n\n'.format(opcoes[opcaoj], opcoes[opcaoPC]))
