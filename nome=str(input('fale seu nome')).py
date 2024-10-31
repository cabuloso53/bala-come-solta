nome=str(input('fale seu nome' ))
nome2= (len(nome)) 
idade=int(input('fale sua idade' ))
salario=int(input('fale seu salario '))
genero=str(input('fale seu genero'))
estado=str(input('Digite seu estado civil S,Solteiro,C,Casado,V,Viuvo,D,Divorciado'))
if nome2 <= 3:
    print('o nome digitado possui 3 ou menos caracteres')
if idade<150 and idade>0:
    print (idade)
else:
    print('a idade digitada e menor que 0 ou maior que 150 ou digitada de maneira incorreta')
if salario>0:
    print(salario)             
else:
    print('o valor digitado e invalido ou menor que 0')
if genero=='homem' or genero=='mulher':
    print(genero)           
else:
    print('o genero digitado esta incorreto')
if estado=='S' or estado=='C' or estado=='V' or estado=='D':
    print (estado)           
else:
    print('o estado civil digitado esta invalido')    
            
        
        
        
        #estado civil s c v d