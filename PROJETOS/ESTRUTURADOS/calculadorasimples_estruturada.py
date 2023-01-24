import math
import os

# FUNÇÕES
soma = lambda n1,n2: n1+n2
subtracao =  lambda n1,n2: n1-n2
multiplicacao = lambda n1,n2: n1*n2
divisao = lambda n1,n2: n1/n2
exponenciacao = lambda n1,n2: math.pow(n1,n2)

operacoes = {
    "+": "SOMA",
    "-": "SUBTRAÇÃO",
    "*": "MULTIPLICAÇÃO",
    "/": "DIVISÃO",
    "**": "EXPONENCIAÇÃO",
    "5": "FECHAR PROGRAMA"
}

lista_chaves = list(operacoes.keys())
lista_valores = list(operacoes.values())


def mostrar_operacoes():
    i = 0
    while (i < 5):
        os.system("cls")
        for nome in operacoes.values():
            print(i, ":", nome,"\n")
            i += 1
            
def inserir_numeros():
    numeros = []
    for i in range(2):
        numeros.append(float(input("Digite o {}º número:\n".format(i+1))))
    return numeros


print("===================== CALCULADORA =====================\n\n")

mostrar_operacoes()

escolha = int(input("Escolha uma operação:\n"))
resposta = 1

while (escolha != 5 and resposta != 0):
    print("Você escolheu {}\n".format(lista_valores[escolha]))

    numeros = inserir_numeros()

    if (escolha == 0):
        resultado = soma(numeros[0],numeros[1])
        print("\n\t{} {} {} = {}\n".format(numeros[0],lista_chaves[escolha],numeros[1],resultado))
        
    elif (escolha == 1):
        resultado = subtracao(numeros[0],numeros[1])
        print("\n\t{} {} {} = {}\n".format(numeros[0],lista_chaves[escolha],numeros[1],resultado))

    elif (escolha == 2):
        resultado = multiplicacao(numeros[0],numeros[1])
        print("\n\t{} {} {} = {}\n".format(numeros[0],lista_chaves[escolha],numeros[1],resultado))
        
    elif (escolha == 3):
        resultado = divisao(numeros[0],numeros[1])
        print("\n\t{} {} {} = {}\n".format(numeros[0],lista_chaves[escolha],numeros[1],resultado))
        
    elif (escolha == 4):
        resultado = exponenciacao(numeros[0],numeros[1])
        print("\n\t{} {} {} = {}\n".format(numeros[0],lista_chaves[escolha],numeros[1],resultado))

    resposta = int(input("Deseja fazer outra operação? 0 - Não /  1 - Sim\n"))
    
    if (resposta == 1):
        os.system("cls")
    
        print("===================== CALCULADORA =====================\n\n")

        mostrar_operacoes()

        escolha = int(input("Escolha uma operação:\n"))
    




    

