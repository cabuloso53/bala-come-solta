#Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros.
#Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

i=0
while i>2:
    aluno=int(input('Fale seu número: '))
    alturaDOaluno=float(input('Fale sua altura em centímetros'))
    i+=1
    if alturaDOaluno>alturaDOaluno:
        print('O aluno mais alto é o número',aluno,alturaDOaluno)