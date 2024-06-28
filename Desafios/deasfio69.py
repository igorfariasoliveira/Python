idade = maiorIdade = homens = mulherMenor = 0
sexo = None
while True:
  print('-'*20)
  print('CADASTRO DE PESSOA')
  print('-'*20)
  idade = int(input('Idade: '))
  sexo = str(input('Sexo(M/F): ')).lower()
  if idade > 18:
    maiorIdade+=1
  if sexo == 'm':
    homens+=1
  if sexo == 'f' and idade <20:
    mulherMenor+=1
  print(maiorIdade,homens,mulherMenor)
  