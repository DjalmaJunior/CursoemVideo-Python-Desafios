# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

# Método para transformar decimal em binário -------------------------------------------------------------
def d_b(n):
    st = ''  # String que armazena o numero binario
    binario = []  # Lista para armazenar os numeros das divisões
    while True:
        if n % 2 == 0:
            binario.append(0)
        else:
            binario.append(1)
        n = n // 2
        if n == 1:
            if n % 2 == 0:
                binario.append(0)
            else:
                binario.append(1)
            break
    for s in list(reversed(binario)):
        st += str(s)  # Converte para string os valores passados como int e faz a concatenação entre eles
    return st
# ---------------------------------------------------------------------------------------------------------


# Método para transformar decimal em octal ---------------------------------------------------------------
def d_o(n):
    octal = []  # Lista para armazenar os restos das divisões e, por fim, o valor do ultimo quociente
    st = ''  # String que armazena o numero octal
    octal.append(n % 8)  # Armazena o primeiro resto da divisão
    while True:
        n = n // 8
        if n > 8:
            octal.append(n % 8)
        else:
            octal.append(n)
            break
    for s in list(reversed(octal)):
        st += str(s)  # Converte para string os valores passados como int e faz a concatenação entre eles
    return st


# --------------------------------------------------------------------------------------------------------

# Método para transformar decimal em hexadecimal ------------------------------------------------------------------------
def d_h(n):
    # Valores atribuidos as letras na base hexadecimal
    A = 10
    B = 11
    C = 12
    D = 13
    E = 14
    F = 15
    # -------------------------------------------------

    st = ''  # String que armazena o numero hexadecimal
    hexa = []  # Lista para armazenar os restos das divisões e, por fim, o valor do ultimo quociente
    # Verificando se o valor do resto da divisão deve ser substituido pela letra a qual esteja representado anteriormente
    if n % 16 == A:
        hexa.append('A')
    elif n % 16 == B:
        hexa.append('B')
    elif n % 16 == C:
        hexa.append('C')
    elif n % 16 == D:
        hexa.append('D')
    elif n % 16 == E:
        hexa.append('E')
    elif n % 16 == F:
        hexa.append('F')
    else:
        hexa.append(n % 16)
    while True:
        n = n // 16
        if n >= 16:
            if n % 16 == A:
                hexa.append('A')
            elif n % 16 == B:
                hexa.append('B')
            elif n % 16 == C:
                hexa.append('C')
            elif n % 16 == D:
                hexa.append('D')
            elif n % 16 == E:
                hexa.append('E')
            elif n % 16 == F:
                hexa.append('F')
            else:
                hexa.append(n % 16)
        else:
            if n == A:
                hexa.append('A')
                break
            elif n == B:
                hexa.append('B')
                break
            elif n == C:
                hexa.append('C')
                break
            elif n == D:
                hexa.append('D')
                break
            elif n == E:
                hexa.append('E')
                break
            elif n == F:
                hexa.append('F')
                break
            else:
                hexa.append(n)
                break
    for s in list(reversed(hexa)):
        st += str(s)  # Converte para string os valores passados como int e faz a concatenação entre eles
    return st


# -----------------------------------------------------------------------------------------------------------------------

# Entrada de valor inteiro -------------------------------
while True:
    try:
        num = int(input('Informe um número inteiro: '))
        break
    except ValueError:
        print('Somente inteiros!!')
# --------------------------------------------------------

# Entrada e impressão da opção escolhida para converter o valor decimal -------------------------------------------------------------------------
while True:
    try:
        conversao = int(input('Qual será a conversão desejada? (1 - binário) || (2 - octal) || (3 - hexadecimal)\n'))  # Entrada da conversão desejada
        # Retornando uma exceção ao receber uma entrada diferente das disponíveis
        if conversao != 1 and conversao != 2 and conversao != 3:
            conversao = int('a')
        break
    except ValueError:
        print('As opções são apenas 1, 2 ou 3!!')
if conversao == 1:
    print('O número {0} convertido em binário é: {1}'.format(num, d_b(num)))
elif conversao == 2:
    print('O número {0} convertido em octal é: {1}'.format(num, d_o(num)))
elif conversao == 3:
    print('O número {0} convertido em hexadecimal é: {1}'.format(num, d_h(num)))

# -----------------------------------------------------------------------------------------------------------------------------------------------
