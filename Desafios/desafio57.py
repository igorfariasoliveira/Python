sexo = ''
while sexo != 'm' and sexo != 'f':
  sexo = str(input('Qual o seu sexo?(M/F) ')).lower().strip()
  if sexo != 'm' and sexo != 'f':
    print('Comando incorreto. Digite M para masculino e F para feminino')
print('Obrigado')