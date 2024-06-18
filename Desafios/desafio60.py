num = int(input('Digite um número para fatorar: '))
fat = 1
cont = num
while cont > 1:
  fat *= cont
  cont -= 1
print('O fatorial é {}'.format(fat))