# Crie um programa que, dado o nome completo de alguém, cumprimente tal pessoa por seu primeiro nome

def cumprimento(nome):
    nome = nome.split()
    return nome[0]

nome = str(input("Digite seu nome: "))
print("Olá, senhor(a) {}".format(cumprimento(nome)))

