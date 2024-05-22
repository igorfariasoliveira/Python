vel = int(input('Em que velocidade você está? '))
if vel > 80:
  multa = (vel - 80)*7
  print('Seu carro está acima da velocidade permitida!')
  print('Terá que pagar uma multa de {}R$'.format(multa))
else:
  print("Você não está acima da velocidade")