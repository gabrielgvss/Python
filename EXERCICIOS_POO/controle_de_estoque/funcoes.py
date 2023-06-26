import classe


def menu():
    print("1 - CADASTRO DE PRODUTO")  # Create
    print("2 - EDITAR PRODUTO")  # Update and Delete
    print("3 - ACRESCENTAR MERCADORIA AO ESTOQUE")
    print("4 - VISUALIZAR MERCADORIAS")  # Read
    print("5 - VISUALIZAR RELATÓRIO DE OPERAÇÕES")
    print("Escolha sua opção:\n")


def cadastro():
    print("---------------- CADASTRO DE PRODUTO -----------------\n")
    while True:
        try:
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            qtd = int(input("Digite a quantidade do produto em estoque: "))
            break

        except ValueError:
            print("ERRO NO CADASTRO! CERTIFIQUE-SE DE UTILZIAR VALORES NUMÉRICOS PARA PREÇO E QUANTIDADE.")
            print("----------------------------------------------\n")

    produtos.append(classe.Produto(nome, preco, qtd))
