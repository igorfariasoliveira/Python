from datetime import datetime
ano_atual = datetime.now().year
nasc = int(input('Em que ano você nasceu?'))
if (ano_atual-nasc) < 18:
  alistamento = ano_atual - nasc - 18
  print('Você ainda vai se listar no exercito daqui há {} anos'.format(alistamento))
elif (ano_atual-nasc) > 18:
  vencimento = (ano_atual - nasc - 18)*(-1)
  print('Você ja deveria ter se alistado há {} anos'.format(vencimento))
else:
  print('Voce deve se alistar esse ano!')