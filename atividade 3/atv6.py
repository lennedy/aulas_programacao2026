def analisar_notas():
    contador=0
    contador1=0
    soma=0
    for i in range (5):
        notas = float(input("diga as notas: "))
        soma += notas

        if notas >=6:
            contador+=1

        elif notas <= 6:
            contador1+=1

    media = soma/5


    print("numero de alunos com notas maior ou igual a 6: ", (contador))
    print("numero de alunos com notas menor ou igual a 6: ", (contador1))


    print("media das notas ", (media))



analisar_notas()

