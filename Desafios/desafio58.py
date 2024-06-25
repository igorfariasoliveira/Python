from random import randint
numero_aleatorio = None
num = 0
contador = 0
while numero_aleatorio != num:
  numero_aleatorio = randint(0,10)
  num = int(input('Advinha o número que estou pensando entre 0 e 10... '))
  contador += 1
  if numero_aleatorio != num:
    print('Eu pensei no número {}. Você errou, mas pode tentar novamente!'.format(numero_aleatorio))
print('Parabéns, você acertou em {} jogadas!'.format(contador)) 