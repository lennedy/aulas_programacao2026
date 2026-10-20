temperatura = int(input (' Informe a temperatura: '))
a = 0
soma = 0 


menor = temperatura
maior = temperatura


while temperatura != -999 :
    soma = soma + temperatura

    if temperatura > maior:
        maior = temperatura

    if  temperatura < menor :
        menor = temperatura

    temperatura = int(input (' Informe a temperatura: '))
    a += 1



 
print( "a maior temperatura é :", (maior), "a menor temperatura é:" , (menor))

media = soma/a

print("media: " , (media))
print("quantidade de temperatura fornecidas: ", (a))
print("soma das temperaturas: ", (soma), "graus celsius")




