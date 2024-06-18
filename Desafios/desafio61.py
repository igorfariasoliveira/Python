primeiro = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
c = 0
res = 0
while c < 10:
  res = primeiro + c*razao
  c+=1
  print(res)