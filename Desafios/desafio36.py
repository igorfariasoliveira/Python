valor = int(input('Qual o valor do imóvel? '))
salario = float(input('Quanto você recebe de salário? '))
tempo = int(input('Em quantos anos você deseja quitar essa compra? '))
parcelas = valor/(tempo*12)
credito = salario*0.30
if credito <= parcelas:
  print('Parabéns, sua compra foi aprovada. Você pagará parcelas de {:.2f}'.format(parcelas))
else