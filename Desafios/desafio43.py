from time import sleep
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso/(pow(altura,2))
print('Calculando ...')
sleep(2)
if imc < 18.5:
  print('Seu imc é {:.1f}. Você está abaixo do peso!'.format(imc))
elif imc >= 18.5 and imc < 25:
  print('Seu imc é {:.1f}. Você está com o peso ideal!'.format(imc))
elif imc >= 25 and imc < 30:
  print('Seu imc é {:.1f}. Você está com sobrepeso!'.format(imc))
elif imc >= 30 and imc < 40:
  print('Seu imc é {:.1f}. Você está com obesidade!'.format(imc))
else:
  print('Seu imc é {:.1f}. Você com obesidade morbida!'.format(imc))
