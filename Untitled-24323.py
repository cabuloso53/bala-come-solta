for i in range(5):
    cliente=str(input('nome do cliente '))
    endereco=str(input('endereço do cliente '))
    valor=int(input('valor da compra '))
    if valor > 50000:
        n1 = (valor / 15)+valor
    if valor <= 50000:
        n1 = (valor / 10)+valor
    print('valor teve um aumento de',n1)



