# Crie um programa que tem como input o salário pot hora de alguém junto a quantidade de horas trabalhadas.
# Calcule e mostre seu salário mensal, levando em consideração:
# Deduções: 11% de IR, 8% de INSS, 5% de taxa sindical (MOSTRE O VALOR TOTAL DE CADA DEDUÇÃO)

def deducao_IR(salario_bruto):
    deducao = (salario_bruto * 0.11)
    return deducao


def deducao_INSS(salario_bruto):
    deducao = (salario_bruto * 0.08)
    return deducao


def deducao_sindical(salario_bruto):
    deducao = (salario_bruto * 0.05)
    return deducao


salario_hora = float(input("Digite o quanto você ganha por hora trabalhada: R$ "))
qtd_horas = int(input("Digite a quantidade de horas trabalhadas: "))

salario_bruto = (salario_hora * float(qtd_horas))

deducao_total = ((deducao_INSS(salario_bruto) + 
                                 deducao_IR(salario_bruto) + 
                                 deducao_sindical(salario_bruto)))

salario_liquido = (salario_bruto - deducao_total)

print("SALÁRIO BRUTO: R$ {:.2f}".format(salario_bruto))
print("DEDUÇÃO IR: R$ {:.2f}".format(deducao_IR(salario_bruto)))
print("DEDUÇÃO INSS: R$ {:.2f}".format(deducao_INSS(salario_bruto)))
print("DEDUÇÃO SINDICAL: R$ {:.2f}".format(deducao_sindical(salario_bruto)))
print("\nDEDUÇÃO TOTAL: R$ {:.2f}".format(deducao_total))
print("\nSALÁRIO LÍQUIDO: R$ {:.2f}".format(salario_liquido))
