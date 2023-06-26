#CRIAR PROGRAMA DE REGISTROS DE HOTEL (CADASTRO DE CPF E NOME POR QUANTIDADE DE PESSOAS NO QUARTO)
#GERAR LISTA 
import os
hospedes = []

os.system("cls")
print("-------------- CADASTRO ---------------")
qtd_pessoas = int((input("Insira a quantidade de pessoas por quarto: ")))

for i in range(qtd_pessoas):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    cpf = input(f"Digite o cpf da {i+1}ª pessoa: ")
    cadastro = [nome, f"CPF: {cpf}"]
    
    hospedes.append(cadastro)
    
print(hospedes)
    
    
                 
