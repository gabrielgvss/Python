# Crie uma programa que dada uma plavra de entrada determine se esta é ou não um palíndromo


palindromo = str(input("Digite uma palavra ou frase para saber se a mesma é palíndromo ou não:\n"))

if (str.upper(palindromo[::-1]) == str.upper(palindromo)):
    print(f"{palindromo} é um palindromo")
else:
    print(f"{palindromo} não é um palindromo")
        

    
    