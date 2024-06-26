from random import randint

while True:
  jog = int(input('Escolha um número: '))
  comp = randint(0,99)
  esco = str(input('Você quer par ou impar?(P/I) ')).lower()
  soma = comp + jog
  if soma % 2 == 0:
    