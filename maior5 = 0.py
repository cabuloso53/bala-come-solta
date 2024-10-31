maior5 = 0
maior2 = 0
maior3 = 0

menor1 = 0
menor2 = 0
menor44 = 0
for i in range(1, 3):
    idade = int(input('idade: '))
    peso = int(input('peso: '))
    altura = int(input('altura: '))
    if  idade > maior5:
        maior5 = idade
    if  peso > maior2:
        maior2 = peso
    if  altura > maior3:
        maior3 = altura
    if  idade < menor1:
        menor1 = idade
    if  peso < menor2:
        menor2 = peso
    if  altura < menor44:
        menor44 = altura
print('A maior idade lido foi',maior5)
print('O maior peso lido foi ',maior2)
print('A maior altura lido foi',maior3)
print('A menor idade lido foi',menor1)
print('O menor peso lido foi ',menor2)
print('A menor altura lido foi',menor44)
