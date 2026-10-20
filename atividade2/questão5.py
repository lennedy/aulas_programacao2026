valor = 1000.00

while True:

    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("consultar saldo ")
        print (valor)

    elif opcao == 2:
        print("Depositar saldo")
        deposito = float(input( " digite o valor do deposito:"))
        valor += deposito
        print ( "deposito realizado, seu saldo agora é:", (valor))

    elif opcao == 3:
        print("Sacar")
        saque = float(input("Digite o valor de saque: "))
        if saque <= valor:
            valor = valor - saque 
            print("voce sacou: reais", (saque), "\nseu saldo agora é:", (valor))

        else :
            print("saldo insuficiente para o seu saque")

    elif opcao == 4:
        print("Saindo...")
        break
        
    else:
        print("Opção inválida")