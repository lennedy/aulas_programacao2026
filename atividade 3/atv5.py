def mostrar_pares():
    contador=0
    numero = int(input("me diga um numero: "))


    for i in range(1, numero + 1):
        
        if i % 2 == 0:
            contador+=1

            print(i)

    print('existe', (contador), 'numeros pares')
          

mostrar_pares()
