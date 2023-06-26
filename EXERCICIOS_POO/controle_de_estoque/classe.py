import random

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.codigo = None
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.operacoes = []

    def acrescenta_operacao(self, operacao):
        self.operacoes.append(operacao)

    def gera_codigo(self):
        codigo = random.randint(1000, 10000)
        while codigo in codigos:
            codigo = random.randint(1000, 10000)

        self.codigo = random.randint(1000, 10000)

    def altera_nome(self, novo_nome):
        self.nome = novo_nome

    def altera_preco(self, novo_preco):
        preco_antigo = self.preco
        self.preco = novo_preco
        self.acrescenta_operacao(f"ALTERAÇÃO DO PREÇO DO PRODUTO '{self.nome}'\n"
                                 f"VALOR ANTIGO: R${preco_antigo}\tNOVO VALOR: R${self.preco}")

    def diminui_quantidade(self, qtd_diminuida):
        if self.quantidade - qtd_diminuida < 0:
            print("ESTOQUE INSUFICIENTE PARA TAL OPERAÇÃO!")

        else:
            self.quantidade -= qtd_diminuida
            self.acrescenta_operacao(f"DECRÉSCIMO DE {qtd_diminuida} UNIDADES DO PRODUTO '{self.nome}'")

    def aumenta_quantidade(self, qtd_aumentada):
        self.quantidade += qtd_aumentada
        self.acrescenta_operacao(f"ADIÇÃO DE {qtd_aumentada} UNIDADES DO PRODUTO '{self.nome}'")