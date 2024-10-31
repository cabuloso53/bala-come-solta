from random import randint
itens = ('pedra' , 'papel' , 'tesoura')
computador = randint(0, 2)
print('''Suas opçoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador=int(input('Qual e a sua jogada?'))
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))  
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)
if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print(' Empatou ')
    elif jogador == 1:
        print('jogador vence')
    elif jogador == 2:
        print('computador vence')
    else:
     print('jogada invalida')
elif computador == 1:# Computador jogou PAPEL
    if jogador == 0:
        print('computador vence')
    elif jogador == 1:
        print('empate')
    elif jogador == 2:
        print('jogador vence')
    else:
     print('jogada invalida')
elif computador == 2:# Computador jogou TESOURA
    if jogador == 0:
        print('jogador vence')
    elif jogador == 1:
        print('computador vence')
    elif jogador == 2:
        print('empate')
    else:
     print('fora do jogo')