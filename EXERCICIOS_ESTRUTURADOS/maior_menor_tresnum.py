numeros = []
contador_de_numeros_iguais = 0

for i in range(3):
    numeros.append(float(input("Digite o {}º número:\n".format(i+1))))
    
maior_numero = numeros[0]
menor_numero = numeros[0]

for i in numeros:
    if maior_numero < i:
        maior_numero = i
numeros.remove(maior_numero)
   
for j in numeros:
    if menor_numero > j:
        menor_numero = j
numeros.remove(menor_numero)
        
print("MAIOR NÚMERO: {}\nMENOR NÚMERO: {:.5f}".format(maior_numero, menor_numero))
print("\nNÚMERO DO MEIO: {}".format(numeros[0]))
