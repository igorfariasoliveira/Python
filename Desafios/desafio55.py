maior = None
menor = None
for c in range(1,6):
  peso = float(input('Peso da {}ª pessoa: '.format(c)))
  if maior is None or peso > maior:
    maior = peso
  if menor is None or peso < menor:
    menor = peso
print('O maior peso é {:.1f}kg e o menor é {:.1f}kg'.format(maior,menor))