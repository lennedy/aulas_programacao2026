n = int(input('digite um numero inteiro e positivo:'))
soma = 0

for i in range (n+1):
    
    if i % 2 == 0:
        soma = soma + i 
        print ("numeros pares:", i)

print(soma)

