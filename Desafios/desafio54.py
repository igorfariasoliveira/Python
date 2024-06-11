from datetime import datetime
maior = 0
menor = 0
ano_atual = datetime.now().year
for c in range(1,8):
  nasc = int(input('ano de nascimento da {}° pessoa: '.format(c)))
  idade = ano_atual - nasc
  if idade >= 18:
    maior+=1
  else:
    menor+=1
print('Das sete pessoas informadas {} são menores de idade e {} são maiores de idade!'.format(menor,maior))