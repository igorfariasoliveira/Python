maior = 0
menor = None
for c in range(0,5):
  peso = float(input('Qual o seu peso?'))
  if peso > maior:
    maior = peso
  if menor is None or peso < menor:
    menor = peso
