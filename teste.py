tipo = str(input('Escolha qual o tipo do pokêmon inicial você vai escolher entre água, fogo e planta ')).lower()
if tipo == 'água' or tipo == 'agua':
  pokemon = int(input('Você deve escolher entre:\n1: Squirtle\n2: Totodile\n3: Mudkip\nDigite o número do pokemon correspondente: '))
  if pokemon == 1:
    print('Parabéns! Você escolheu o pokemon Squirtle da região de Kanto. Boa sorte na sua jornada ')
