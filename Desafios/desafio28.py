import random
numero_aleatorio = random.randint(0,5)
num = int(input('Advinha o número que estou pensando entre 0 e 5... '))
print('O numero que pensei foi {}'.format(numero_aleatorio))
if numero_aleatorio == num:
  print('Parabéns! Você acertou')
else:
  print('Que pena! Você errou')