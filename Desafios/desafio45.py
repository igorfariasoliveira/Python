from random import choice
print('Vamos jogar pedra, papel e tesoura?')
jogador = str(input('Qual você vai jogar? ')).lower()
nomes = ['pedra','papel','tesoura']
computador = choice(nomes)
if computador == jogador:
  print('-=' * 21)
  print('Eu tambem escolhi {}. Deu empate'.format(computador))
  print('-=' * 21)
elif (jogador == 'pedra' and computador == 'papel') or (jogador == 'tesoura' and computador == 'pedra') or (jogador == 'papel' and computador == 'tesoura'):
  print('-=' * 21)
  print('Eu escolhi {}. Eu ganhei!'.format(computador))
  print('-=' * 21)
elif (jogador == 'pedra' and computador == 'tesoura') or (jogador == 'tesoura' and computador == 'papel') or (jogador == 'papel' and computador == 'pedra'):
  print('-=' * 21)
  print('Eu escolhi {}. Parabéns, você ganhou!'.format(computador))
  print('-=' * 21)
else:
  print('Você não escolheu pedra, papel ou tesoura. Tente novamente!')
print('')