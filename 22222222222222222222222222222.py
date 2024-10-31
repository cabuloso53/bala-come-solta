n=int(input('digite um numero inteiro:'))
if n>1:
    for i in range (2,n):
        if (n%i==0):
            print('nao e primo')
        else:
            print('e numero primo')
    else:
        print('nao e numero primo')