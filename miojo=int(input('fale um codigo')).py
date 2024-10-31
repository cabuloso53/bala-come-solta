n1=int(input('digite um codigo: '))
n2=int(input('fale o total de vendas: '))
if(n2<=100):
    print('a comissao foi de 0%', n2)
elif(n2>100)and(n2<=350):
    a=(n2/6)+n2
    print('a comissao foi de 6%',a)
elif(n2>350):
    a2=(n2/10)+n2
    print('a comissao foi de 10%',a2)
    