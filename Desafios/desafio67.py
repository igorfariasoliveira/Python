c = 1
num = 0
while True:
  num = int(input('Qual o valor você deseja ver a tabuada? '))
  while c <=10:
    print(f"{num} x {c} = {num*c}")
    c+=1
  c=1
  if num < 0:
    break