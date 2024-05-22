salario = float(input('Qual o seu salario? '))
if salario > 1250:
  aumento = (salario*0.10) + salario
  print('seu novo sálario será de {:.2f} reais'.format(aumento))
else:
  aumento = (salario*0.15) + salario
  print('Seu novo sálario será de {:.2f} reais'.format(aumento))