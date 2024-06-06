maior = none
menor = None
for c in range(0,5):
  peso = float(input('Qual o seu peso?'))
  if maior is None or peso > maior:
    maior = peso
  if menor is None or peso < menor:
    menor = peso
print('O maior peso é {}kg e o menor é {}kg'.format(maior,menor))