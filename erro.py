from time import sleep
from random import randint

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
jogada = int(input('Qual a sua jogada? '))

if jogada not in [0, 1, 2]:
    print('JOGADA INVÁLIDA! TENTE NOVAMENTE!')
else:
    print('JO'), sleep(0.5)
    print('KEN'), sleep(0.5)
    print('PO!!!')
    print(f'''{'=':=^20}
Computador jogou {itens[pc]}
Jogador jogou {itens[jogada]}
{'=':=^20}''')

    if jogada == 0 and pc == 1:
        print('COMPUTADOR VENCE!')
    elif jogada == 0 and pc == 2:
        print('JOGADOR VENCE!')
    elif jogada == 1 and pc == 0:
        print('JOGADOR VENCE!')
    elif jogada == 1 and pc == 2:
        print('COMPUTADOR VENCE!')
    elif jogada == 2 and pc == 0:
        print('COMPUTADOR VENCE!')
    elif jogada == 2 and pc == 1:
        print('JOGADOR VENCE!')
    elif jogada == pc:
        print('EMPATE!')