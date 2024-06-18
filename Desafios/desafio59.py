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
      print('O número maior é {}'.format(n1))
    elif n2>n1:
      print('O número maior é {}'.format(n2))
    else:
      print('Ambos os numeros fornecidos são iguais!')
  elif escolha == 4:
    print('Teste')
  else: 
    print('Opção invalida. Por favor escolha um número dentre as opções fornecidas')