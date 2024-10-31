cont = 0
cont2 = 0
cont3 = 0
cont4 = 0
for i in range(5):
    roupa = str(input('qual o tamanho da camisa: '))
    if roupa == 'p':
        cont += 1
    elif roupa == 'm':
        cont2 += 1
    elif roupa == 'g':
        cont3 += 1
    elif roupa == 'gg':
        cont4 += 1
print('roupas p',cont)
print('roupas m',cont2)
print('roupas g',cont3)
print('roupas gg',cont4)
