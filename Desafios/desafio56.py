idade_grupo = 0
mais_velho = None
nome_velho = None
contador_fem = 0
for c in range(0,4):
  nome = str(input('Qual o seu nome? '))
  idade = int(input('Qual a sua idade? '))
  sexo = int(input('Se seu sexo for masculino digite 1. Se for feminino digite 2. '))
  idade_grupo += idade
  if mais_velho is None or idade > mais_velho:
     mais_velho = idade
     nome_velho = nome
  if sexo == 2:
    contador_fem+=1
media = idade_grupo/4
print(media)
print(nome_velho)

