idade_grupo = 0
mais_velho = None
nome_velho = None
for c in range(0,4):
  nome = str(input('Qual o seu nome? '))
  idade = int(input('Qual a sua idade? '))
  idade_grupo += idade
  if mais_velho is None or idade > mais_velho:
     mais_velho = idade
     nome_velho = nome
media = idade_grupo/4
print(media)
print(nome_velho)
