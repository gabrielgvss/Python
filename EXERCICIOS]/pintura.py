# Faça um programa para uma loja de tintas. A pessoa informa a área em m² que deseja pintar e o script calculará
# a quantidade de latas de tinta que a pessoa deve comprar e o valor total.
# Cada litro pinta 3m², cada lata tem 18L e o preço da unidade é igual a R$80.
import math


def quantidadeLatas(area):
    qtd_litros = (area/3)
    qtd_latas = int (qtd_litros/18)
    return (qtd_latas)


def valorTotal(qtd_latas):
    valor_total = qtd_latas * 80
    return valor_total

# preco_lata = 80.0
# volume_lata = 18.0

area = float(input("Digite a área em m² que deseja pintar: "))
qtd = quantidadeLatas(area)

print("QUANTIDADE DE LATAS: {}\nVALOR TOTAL: R$ {}".format(
    quantidadeLatas(area), valorTotal(qtd)))
