c = 1
num = 0
while True:
  print('-'*20)
  num = int(input('Qual o valor você deseja ver a tabuada? '))
  print('-'*20)
  if num < 0:
    break
  while c <=10:
    print(f"{num} x {c} = {num*c}")
    c+=1
  c=1
  