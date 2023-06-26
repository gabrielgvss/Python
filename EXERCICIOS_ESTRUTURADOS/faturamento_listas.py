# Descobrir qual mês teve maior faturamento e qual teve o menor
import random

meses = ["JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO",
         "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO"]

faturamento_1semestre = [random.randint(10000, 99999) for _ in range(6)]
# Gerar números aleatórios
faturamento_2semestre = [random.randint(10000, 99999) for _ in range(6)]

print("FATURAMENTO PRIMEIRO SEMESTRE:")
print("\n".join(list(map(str, faturamento_1semestre))))

print("FATURAMENTO SEGUNDO SEMESTRE:")
print("\n".join(list(map(str, faturamento_2semestre))))

geral = faturamento_1semestre + faturamento_2semestre

maior = max(geral)
menor = min(geral)

i_maior = geral.index(maior)
i_menor = geral.index(menor)

geral.sort(reverse=True)


print(f"O MAIOR FATURAMENTO FOI DE R${maior} E OCORREU NO MÊS DE {meses[i_maior]}")
print(f"O MENOR FATURAMENTO FOI DE R${menor} E OCORREU NO MÊS DE {meses[i_menor]}\n")

print("TOP 3 FATURAMENTOS:")
print("\n".join(list(map(str, geral))))
