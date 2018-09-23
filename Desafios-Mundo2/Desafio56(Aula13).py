# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# A média de idade do grupo;
# Qual é o nome do homem mais velho;
# Quantas mulheres têm menos de 20 anos.
idades = []  # Lista que guarda as idades
grupoM = []  # Grupo masculino
grupoF = []  # Grupo feminino
cont = 0  # Contador de mulheres mais novas do que 20 anos
for i in range(4):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(i+1))).lower().strip()
    sexo = str(input('Digite o sexo da {}ª pessoa: '.format(i+1))).lower().strip()
    idades.append(int(input('Digite a idade da {}ª pessoa: '.format(i + 1))))
    if sexo == 'masculino' or 'homem':
        grupoM.append((nome, sexo, idades[i]))
    elif sexo == 'feminino' or 'mulher':
        grupoF.append((nome, sexo, idades[i]))

# Somatorio das idades
sIdades = 0  # Variavel que armazena o valor do somatorio
for c in idades:
    sIdades += c

# Media das idades
media = sIdades/len(idades)

# Contagem de quantas mulheres mais novas do que 20 anos há no grupo
for m in grupoF:
    if m[2] < 20:
        cont += 1
# ------------------------------------------------------------------

# Calculo do homem mais velho ------------------------------------------------
maior = 0  # Inicialização do maior como 0
menor = 0  # # Inicialização do menor como 0
n = ''  # Variavel que ira armazenar o nome do homem mais velho
for M in grupoM:
    # M[2] é referente a posição da idade na lista da pessoa escolhida
    if M[2] > maior:
        maior = M[2]
        # M[0] é referente a posição do nome na lista da pessoa escolhida
        n = M[0]
    elif M[2] < menor:
        menor = M[2]
# -----------------------------------------------------------------------------

print('-'*60)
print('A média de idade do grupo é de {} anos'.format(int(media)))
print('Homem mais velho: {}'.format(n.capitalize()))
if cont != 1:
    print('Há {} mulheres com menos de 20 anos'.format(cont))
else:
    print('Há {} mulher com menos de 20 anos'.format(cont))
