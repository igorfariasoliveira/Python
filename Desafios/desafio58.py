from random import randint
numero_aleatorio = None
num = None
while numero_aleatorio != num:
  numero_aleatorio = randint(0,5)
  num = int(input('Advinha o número que estou pensando entre 0 e 5... '))
  if numero_aleatorio != num:
    print('Eu pensei no número {}. Você errou, mas pode tentar novamente!')
