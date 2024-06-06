idade_grupo = 0
for c in range(0,4):
  nome = str(input('Qual o seu nome? '))
  idade = int(input('Qual a sua idade? '))
  idade_grupo += idade
media = idade_grupo/4
print(media)