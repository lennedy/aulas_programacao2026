def verificar_idade():
    idade = int(input("me informe sua idade "))

    if idade < 12:
        print("voce é uma criança")

    elif idade >=12 and idade <=17:
        print('voce é uma adolecente')

    else:
        print('voce ja é um adulto')

verificar_idade()
