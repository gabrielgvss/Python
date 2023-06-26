
import random

opcoes = ["cara","coroa"]

opcao_usuario = int(input("0 - CARA / 1 - COROA\n\tR = "))
print(f"Você escolheu {opcoes[opcao_usuario]}\n")

resultado = random.choice(opcoes)
print(f"Resultado: {resultado}\n")

if (opcoes[opcao_usuario] == resultado):
    print("\n\tVOCÊ GANHOU!")

else:
    print("\nVOCÊ PERDEU!")


