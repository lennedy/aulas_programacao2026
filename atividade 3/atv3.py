def verificar_aprovacao():
    nota1= float(input("diga sua primeira nota"))
    nota2= float(input("diga sua segunda nota"))

    media = (nota1+nota2) /2

    if media >= 6:
        print("voce foi aprovado")

    elif media >=4 and media <=6:
        print("voce foi reprovado")

    else:
        print("voce foi reprovado")

    print(media)
verificar_aprovacao()