from classe import *
import os

academia = Academia()

def ver_lista(academia):
    if len(academia.halteres) != 0:
        print(academia.listar_halter_disponivel())
        a = input("\nPressione qualquer tecla para prosseguir:\n")

    else:
        print("TODOS OS HALTERES ESTÃO SENDO UTILIZADOS")


def utilizar_halter(academia):
    ver_lista(academia)
    halter_escolhido = int(input("\nDigite o halter que você deseja:\n"))
    academia.usar_halter(halter_escolhido)
    a = input("\nPressione qualquer tecla para prosseguir:\n")


def situacao_porta_halteres(academia):
    print(academia.listar_porta_halteres())


def guardar_halter(academia):
    academia.listar_porta_halteres()
    halter_guardado = int(input("Digite o peso do halter você deseja guardar:\n"))
    posicao = int(input("Digite a posição do peso onde você deseja guardar:\n"))
    academia.devolver_halter(halter_guardado, posicao)
    a = input("\nPressione qualquer tecla para prosseguir:\n")


while True:
    os.system("cls")
    print("1 - VER LISTA DE HALTERES DISPONÍVEIS")
    print("2 - UTILIZAR HALTER")
    print("3 - GUARDAR HALTER")
    print("4 - VER SITUAÇÃO DO PORTA HALTERES")
    escolha = input("\nDigite sua resposta:\n")

    if (escolha == "1"):
        ver_lista(academia)

    elif (escolha == "2"):
        utilizar_halter(academia)

    elif (escolha == "3"):
        guardar_halter(academia)

    elif (escolha == "4"):
        situacao_porta_halteres(academia)
        a = input("\nPressione qualquer tecla para prosseguir:\n")