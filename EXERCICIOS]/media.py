def aprovacao(media):
    if (media <= 7):
        return "REPROVADO"

    elif (media == 10):
        return "APROVADO COM DISTINÇÃO"

    else:
        return "APROVADO"


notas = []
soma = 0

for i in range(3):
    notas.append(float(input("Digite a {}ª nota do aluno:\n".format(i+1))))
    soma+=notas[i]
    
media = soma / 3

print("MÉDIA DO ALUNO: {:.2f}".format(media))
print("\nSITUAÇÃO: {}".format(aprovacao(media)))
