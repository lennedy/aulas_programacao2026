def contagem():
    
    numero = int(input('diga um numero'))   

    if numero <=0:
        print('numero invalido digite outro')
    else:
        for i in range(1, numero+1):
            print (i)

contagem()