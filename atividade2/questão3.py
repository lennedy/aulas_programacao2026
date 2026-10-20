aluno1 = float(input('digite as notas do aluno 1: '))
aluno2 = float(input('digite as notas do aluno 2: '))
aluno3 = float(input('digite as notas do aluno 3: '))
aluno4 = float(input('digite as notas do aluno 4: '))
aluno5 = float(input('digite as notas do aluno 5: '))

valores = [aluno1,aluno2,aluno3,aluno4,aluno5]

alunos_aprovados = 0

soma = aluno1+aluno2+aluno3+aluno4+aluno5

menor= valores[0]
maior = valores[0]

media = soma /5

for valor in valores:
    if valor > maior:
        maior = valor

    if valor < menor:
        menor = valor

    if valor >= 6:
        alunos_aprovados += 1



for i in valores:
    print(i)

print("Os alunos aprovados foram: ", (alunos_aprovados))

print ("A menor nota é : ", (menor), "\nA maior nota é: ",  (maior))
print ("Media: " , (media))

