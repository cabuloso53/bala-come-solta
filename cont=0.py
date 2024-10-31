numero=1
cont=0
cont2=0
cont3=0
cont4=0
while(numero>0):
    numero=int(input('digite um valor' ))
    if(numero>=0)and(numero<25):
        cont+=1
    if(numero>=26)and(numero<50):
        cont2+=1
    if(numero>=51)and(numero<75):
        cont3+=1
    if(numero>=76)and(numero<100):
        cont4+=1
print('o numero digitado esta entre 0 e 25',cont)
print('o numero digitado esta entre 25 e 50',cont2)
print('o numero digitado esta entre 50 e 75',cont3)
print('o numero digitado esta entre 75 e 100',cont4)
        
        

    
   
   
    

    

    