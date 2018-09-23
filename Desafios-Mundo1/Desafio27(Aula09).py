#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
#Ex: Ana Maria de Souza
#Primeiro: Ana
#Ultimo: Souza
n = input('Digite um nome:').strip()
primeiro = n.split()[0]
ultimo = n.split()[len(n.split())-1]
print("""Nome: {0}
Primeiro nome: {1}
Ultimo nome: {2}""".format(n, primeiro, ultimo))