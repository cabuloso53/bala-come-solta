n1 = 0
n2 = 1
print(n1,'→',n2, end='')
cont=3
while True:
    n3 = n1 + n2
    print('→',n3, end='')
    n1= n2
    n2= n3
    cont +=1
    if n3 >= 500:
        break
print('final')