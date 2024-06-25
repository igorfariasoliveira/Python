num = 0
cont = 0
res = 0
while num != 999:
  num = int(input('Digite um número para contagem! (Caso queira parar digite 999) '))
  if num != 999:
    cont+=1
    res+=num
print('Foram contados {} números e a soma desses números foi {}'.format(cont,res))