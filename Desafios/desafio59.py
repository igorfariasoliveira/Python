n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
escolha = None

while escolha != 5:
  escolha = int(input('Escolha uma das opções abaixo:\n[1] Somar\n[2] Mulriplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\n'))
  if escolha == 1:
    soma = n1+n2
    print('\033[92mA soma dos números {} e {} é {}\033[0m'.format(n1, n2, soma))
  elif escolha == 2:
    mult = n1*n2
    print('\033[92mA multiplicação dos números {} e {} é {}\033[0m'.format(n1,n2,mult))
  elif escolha == 3:
    if n1>n2:
      print('O número maios é {}'.format(n1))
    else:
      print('O número maios é {}'.format(n2))
  elif escolha == 4:
    print('Teste')
  else: