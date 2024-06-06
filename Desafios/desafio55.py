maior = None
menor = None
for c in range(0,5):
  peso = float(input('Qual o seu peso?'))
  if maior is None or peso > maior:
    maior = peso
  if menor is None or peso < menor:
    menor = peso
print('O maior peso é {:.2f}kg e o menor é {:.2f}kg'.format(maior,menor))