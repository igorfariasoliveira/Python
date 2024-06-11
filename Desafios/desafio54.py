maior = 0
menor = 0
for c in range(0,7):
  idade= int(input('ano de nascimento da {}° pessoa: '.format(c)))
  if idade >= 18:
    maior+=1
  else:
    menor+=1
print('Das sete pessoas informadas {} são menores de idade e {} são maiores de idade!'.format(menor,maior))