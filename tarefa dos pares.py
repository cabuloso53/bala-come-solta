pares = 0
impares = 0
for i in range(10):
    numero = int(input("digite um número inteiro: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print("quantidade de pares",pares)
print("quantidade de ímpares",impares)
