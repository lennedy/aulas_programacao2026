def validar_numero():
    numero = float(input("me der uma numero"))

    if numero >0:
        print(" esse numero é positivo")

    elif numero < 0:
        print("esse numero é negativo")

    else:
         print('esse nuemero é um 0')

validar_numero()