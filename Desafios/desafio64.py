num = 0
soma = 0
conf = ''
media = 0
contador = 0
maior = None
menor = None
while conf != 'não':
  num = int(input('Digite um valor: '))
  contador+=1
  soma += num
  media = soma/contador
  conf = str(input('Deseja continuar? ')).lower()
  if maior is None or num > maior:
    maior = num
  if menor is None or num < menor:
    menor = num 
print('A média dos valores digitados é {:.2f}'.format(media) )