soma2 = 0
soma = 0
for i in range(5):
    n1=int(input('fale um numero'))
    soma = soma + n1
    media= soma / 5
    if n1 >= 0: 
        soma2 = soma2 + n1
print(media)
print(soma2)
