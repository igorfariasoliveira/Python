n = int(input('Escolha um número: '))
operador= int(input('Escolha um operador:\n(1) = Soma\n(2) = Subtração\n(3) = Multiplicação\n(4) = Divisão\n'))
res = 0
print('-=' * 5)
if operador == 1:
  for c in range(0,10):
    res= c+n
    print('{} + {} = {}'.format(n,c,res))
elif operador == 2:
  for c in range(0,10):
    res= n-c
    print('{} - {} = {}'.format(n,c,res))
elif operador == 3:
  for c in range(0,10):
    res= c*n
    print('{} x {} = {}'.format(n,c,res))
elif operador == 4:
  for c in range(0,10):
    res= c+n
    print('{} + {} = {}'.format(n,c,res))