n = int(input('Escolha um número: '))
operador= int(input('Escolha um operador:\n(1) = Soma\n(2) = Subtração\n(3) = Multiplicação\n(4) = Divisão\n'))
res = 0
print('-=' * 5)
if operador == 1:
  for c in range(0,10):
    res= c+n
    print('{} + {} = {}'.format(n,c,res))
elif ope