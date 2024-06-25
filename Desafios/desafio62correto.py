primeiro = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
c = 0
res = 0
esc = None
confirma = ''
while confirma not in 'não':
  while c < 10 and esc!= 0:
    res = primeiro + c*razao
    c+=1
    print('{} -> '.format(res), end='')
   