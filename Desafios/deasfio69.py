idade = maiorIdade = homens = mulherMenor = 0
sexo = None
confirm = ''
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
  while confirm != 's' and confirm != 'n':
    confirm = str(input('Deseja cadastrar mais uma pessoas?(S/N) ')).lower()
  if confirm == 'n':
      break
  confirm = ''
print('='*6,' FIM DO CADASTRO','='*6)
print(f'Total de pessoas com maias de 18 anos: {maiorIdade}')
print