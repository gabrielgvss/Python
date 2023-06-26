#Crie um cÃ³digo que dado um email, extraia o domÃ­nio do mesmo

def extrair (email):
    dominio = email.split("@")[-1]
    return dominio

email = str(input("Digite um endereÃ§o de email: "))
print("O domÃ­nio deste email Ã© {}".format(extrair(email)))


