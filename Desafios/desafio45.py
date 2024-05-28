from random import choice
print('Vamos jogar pedra, papel e tesoura?')
jogador = str(input('Qual você vai jogar? ')).lower()
nomes = ['pedra','papel','tesoura']
computador = choice(nomes)
if computador == jogador:
  print('Eu tambem escolhi {}. Deu empate'.format(computador))
elif (jogador == 'pedra' and computador == 'papel') or (jogador == 'tesoura' and computador == 'pedra') or (jogador == 'papel' and computador == 'tesoura'):
  print('Eu escolhi {}. Eu ganhei!'.format(computador))
elif (jogador == 'pedra' and computador == 'tesoura') or (jogador == 'tesoura' and computador == 'papel') or (jogador == 'papel' and computador == 'pedra'):
  print('Eu escolhi {}. Parabéns, você ganhou!'.format(computador))
else:
  print('Você não escolheu pedra, papel ou tesoura. Tente novamente!')