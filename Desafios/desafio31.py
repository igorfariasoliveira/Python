dis = int(input('Qual a distancia da viagem? '))
if dis <= 200:
  total = dis*0.50
  print("Na sua viagem você irá pagar R${}".format(total))
else:
  total = dis*0.45
  print("Na sua viagem você irá pagar R${}".format(total))
  