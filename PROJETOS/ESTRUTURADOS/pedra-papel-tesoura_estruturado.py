import pdb
import os
import random


opcoes = ["PEDRA", "PAPEL", "TESOURA"]
regra_jogo = {
    "PEDRA":"TESOURA",
    "PAPEL":"PEDRA",
    "TESOURA":"PAPEL"
}
contador_usuario = 0
contador_cpu = 0

escolha = 1

os.system("cls")
nome_usuario = str(input("Digite seu nome para começar o jogo:\nR = "))

while(escolha == 1):
    os.system("cls")
    
    for i, opcao in enumerate(opcoes):
        print(f"{i} - {opcao}\n")

    opcao_escolhida = int(input(f"{nome_usuario}, digite a opção desejada e dispute com a CPU:\nR = "))
    print(f"\n{nome_usuario} escolheu {opcoes[opcao_escolhida]}!\n")

    opcao_sorteada = random.choice(opcoes)
    print(f"\nCPU: {opcao_sorteada}\n")
    
    if (opcoes[opcao_escolhida] == opcao_sorteada):
        print(f"EMPATE!\nPLACAR:\n{nome_usuario}: {contador_usuario}\tCPU: {contador_cpu}")
    
    else:
        if (opcao_sorteada == regra_jogo[opcoes[opcao_escolhida]]):
            contador_usuario +=1
            print(f"{nome_usuario} GANHOU!\nPLACAR:\n{nome_usuario}: {contador_usuario}\t\tCPU: {contador_cpu}")

        else:
            contador_cpu +=1
            print(f"CPU GANHOU!\nPLACAR:\n{nome_usuario}: {contador_usuario}\t\tCPU: {contador_cpu}")
        
   
    escolha = int(input("\nDeseja mais uma rodada? 0 - NÃO / 1 - SIM\nR = "))
    
os.system("cls")
print(f"PLACAR FINAL:\n{nome_usuario}: {contador_usuario}\n\nCPU: {contador_cpu}\n")

if (contador_cpu == contador_usuario):
    print("\nO JOGO TERMINOU EMPATE!!")
    
elif (contador_cpu > contador_usuario):
    print("\nCPU GANHOU O JOGO!!")
    
else:
    print(f"{nome_usuario} GANHOU O JOGO!!")

