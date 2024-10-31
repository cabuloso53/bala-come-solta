cont = 0
cont2 = 0
for i in range(5):
    num = int(input('fale um numero'))
    if 10 <= num <= 20:
        cont += 1
    elif num < 10 or num > 20:
        cont2 += 1
print(cont)
print(cont2)
