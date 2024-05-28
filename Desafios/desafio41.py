from datetime import datetime
ano_atual = datetime.now().year
nasc = int(input('Em que ano você nasceu? '))
idade = ano_atual-nasc
if idade <= 9:
  print('Você tem {} anos. Esta na categoria mirim'.format(idade))
elif idade > 9 and idade <= 14:
  print('Você tem {} anos. Esta na categoria infantil'.format(idade))
elif idade > 14 and idade <= 19:
  print('Você tem {} anos. Esta na categoria junior'.format(idade))
elif idade == 20:
  print('Você tem {} anos. Esta na categoria sênior'.format(idade))
else:
  print('Você tem {} anos. Esta na categoria master'.format(idade))