import math
import time
import os

# variáveis principais
carros = [
    {"nome": "Chevrolet Tracker", "preco": 120},
    {"nome": "Chevrolet Onix", "preco": 90},
    {"nome": "Chevrolet Spin", "preco": 150},
    {"nome": "Hyundai HB20", "preco": 85},
    {"nome": "Hyundai Tucson", "preco": 120},
    {"nome": "Fiat Uno", "preco": 60},
    {"nome": "Fiat Mobi", "preco": 70},
    {"nome": "Fiat Pulse", "preco": 130}
]

removidos = []
contador = 0


# funções
def menu():
    os.system("cls")
    print("===============================================")
    print("                   LOCA CAR                    ")
    print("===============================================")
    print("\n\n 1 - MOSTRAR PORTIFÓLIO                    ")
    print("\n\n 2 - ALUGAR CARRO                          ")
    print("\n\n 3 - DEVOLVER CARRO                        ")
    print("\n\n 4 - FECHAR PROGRAMA                       ")
    
    resposta = int(input("\n\nR = "))
    return resposta
    
def mostrar_portfolio():
    
    for i, carro in enumerate(carros):
            if carro['nome'] not in removidos:
                print(f"[{i}] {carro['nome']} {carro['preco']} /dia\n")
        
 
def escolher_veiculo():
    os.system("cls")
    
    print("Dê uma olhada no nosso portfólio:\n\n")
    mostrar_portfolio()
    
    num_veiculo = int(input("Digite o número correspondente ao veículo que você deseja alugar:\nR = "))
    return carros[num_veiculo]['nome'], carros[num_veiculo]['preco']
    
    
def alugar(carro_escolhido, preco_carro):
    num_dias = int(input("Por quantos dias deseja alugar o veículo {}?\nR = ".format(carro_escolhido)))
    
    preco_total = preco_carro * num_dias
    print(f"\nPreço total para aluguel do veículo {carro_escolhido} durante {num_dias} dias: R$ {preco_total}")

    confirmacao = int(input("Deseja confirmar o aluguel? (0 - Não/1 - Sim)\n R = "))
    return confirmacao


def remover_veiculo(carro_escolhido):
    removidos.append(carro_escolhido)
    

def devolver_veiculo():
    for i, veiculo in enumerate(removidos):
        print(f"[{i}] {veiculo}")

    codigo = int(input("\n\nDigite o código do veículo que deseja devolver:\nR = "))
    os.system("cls")
    print(f"\n\n\t Veículo {removidos[codigo]} devolvido com sucesso!")
    removidos.remove(removidos[codigo])
  
    time.sleep(3)
    os.system("cls")
    

# main code
escolha = 0
resposta = 1

while (escolha != 4 and resposta != 0):
    escolha = menu()
    
    #mostrar portfolio
    if (escolha == 1):
        os.system("cls")
        
        mostrar_portfolio()
        resposta = int(input("\n0 - Sair      1 - Continuar\n\nR = "))
        os.system("cls")
    
    #alugar    
    if (escolha == 2):
        veiculo_escolhido, preco_veiculo = escolher_veiculo()
        confirmacao = alugar(veiculo_escolhido,preco_veiculo)
        
        if (confirmacao == 1):
            remover_veiculo(veiculo_escolhido)
            print(f"Veículo {veiculo_escolhido} alugado com sucesso!")
            contador += 1
            time.sleep(3)
            os.system("cls")
    
    #devolver    
    if (escolha == 3 and contador > 0):
        os.system("cls")
        
        devolver_veiculo()
        resposta = int(input("\n0 - Sair      1 - Continuar\n\nR = "))
        
        os.system("cls")
        
    
        
        
        
        

    



