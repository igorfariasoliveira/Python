num = int(input('Digite um número: '))
base = int(input('Você quer em \n 1: Binario\n 2: Octal\n 3: Hexadecimal\nDigite sua escolha: '))
if base == 1:
  binario = bin(num)[2:]
  print('O número {} na base binaria é {}'.format(num,binario))
elif base == 2:
  octal = oct(num)[2:]
  print('O número {} na base octal é {}'.format(num,octal))
elif base == 3:
  hexadecimal = hex(num)[2:]
  print('O número {} na base hexadecimal é "{}"'.format(num,hexadecimal))
else:
  print('Escolha um número entre as opções acima')