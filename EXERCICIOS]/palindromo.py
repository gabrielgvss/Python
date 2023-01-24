# Crie uma programa que dada uma plavra de entrada determine se esta é ou não um palíndromo
# Exemplos de palíndromos: Ama, Arara, Anotaram a data da maratona

palindromo = str(input("Digite uma palavra ou frase paa saber se a mesma é palíndromo ou não:\n"))

if (len(palindromo) <= 2):
    print("{} não é um palíndromo".format(palindromo))  
    
elif (len(palindromo) == 3):
    if(palindromo[-1] == palindromo[0]):
        print("{} é um palíndromo".format(palindromo))
    else:
        print("{} não é um palíndromo".format(palindromo))  
    
    
    