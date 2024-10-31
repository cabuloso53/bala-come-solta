def calcular_media():
    soma = 0
    contador = 0

    while contador < 50:
        numero = float(input("Digite um número: "))
        soma += numero
        contador += 1

    media = soma / 50
    print("A média dos números digitados é:", media)

calcular_media()
