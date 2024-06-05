n = int(input('Digite um número primo: '))
res = 0
for c in range(1,n+1):
  if n % c == 0:
    res+=1
if res == 2:
  print('Esse número é primo')