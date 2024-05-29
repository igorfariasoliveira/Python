tipo = str(input('Escolha qual o tipo do pokêmon inicial você vai escolher entre água, fogo e planta ')).lower()
if tipo == 'água' or tipo == 'agua':
  pokemon = int(input('Você deve escolher entre:\n1: Squirtle\n2: Totodile\n3: Mudkip\nDigite o número do pokemon correspondente: '))
  if pokemon == 1:
    print('Parabéns! Você escolheu o pokemon Squirtle da região de Kanto. Boa sorte na sua jornada! ')
  elif pokemon == 2:
    print('Parabéns! Você escolheu o pokemon Totodile da região de Johto. Boa sorte na sua jornada! ')
  elif pokemon == 3:
    print('Parabéns! Você escolheu o pokemon Mudkip da região de Hoenn. Boa sorte na sua jornada! ')
elif tipo == 'fogo':
  pokemon = int(input('Você deve escolher entre:\n1: Charmander\n2: Cyndaquil\n3: Torchic\nDigite o número do pokemon correspondente: '))
  if pokemon == 1:
    print('Parabéns! Você escolheu o pokemon Charmander da região de Kanto. Boa sorte na sua jornada! ')
  elif pokemon == 2:
    print('Parabéns! Você escolheu o pokemon Cyndaquil da região de Johto. Boa sorte na sua jornada! ')
  elif pokemon == 3:
    print('Parabéns! Você escolheu o pokemon Torchic da região de Hoenn. Boa sorte na sua jornada! ')
elif tipo == 'planta':
  pokemon = int(input('Você deve escolher entre:\n1: Charmander\n2: Cyndaquil\n3: Torchic\nDigite o número do pokemon correspondente: '))