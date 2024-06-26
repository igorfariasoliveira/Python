from random import randint

while True:
  print('-'*20)
  jog = int(input('Escolha um número: '))
  print('-'*20)
  comp = randint(1,99)
  esco = str(input('Você quer par ou impar?(P/I) ')).lower()
  soma = comp + jog
  if soma % 2 == 0:
    if esco == 'p':
      print(f'Você escolheu {jog} e eu {comp}, somando dá {soma} que é um número par')
      print('Parabéns, você venceu!')
    elif esco == 'i':
      print(f'Você escolheu {jog} e eu {comp}, somando dá {soma} que é um número impar')
      print('Que pena. Você perdeu!')
      