n = int(input('Digite um número: '))
if n < 2:
    print('O número {} não é primo!'.format(n))
else:
  res = 0
  for c in range(1,n+1):
    if n % c == 0:
      res+=1
  if res == 2:
    print('O número {} é primo!'.format(n))
  else:
    print('O numero {} não é primo!'.format(n))