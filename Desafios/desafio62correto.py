primeiro = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
c = 0
res = 0
esc = None
termos = 10
total = 0
while termos != 0:
  total = total + termos
  while c < total and esc!= 0:
    res = primeiro + c*razao
    c+=1
    print('{} -> '.format(res), end='')
  termos = int(input('Deseja adcionar mostrar mais termos? '))
   