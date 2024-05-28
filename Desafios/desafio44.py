preco = float(input('Qual o valor do produto? '))
opcao = int(input("Selecione a opçao de pagamento:\n1: dinheiro ou cheque\n2: cartão de credito\n"))
if opcao == 1:
  total = preco-(preco*0.10)
  print('Com o desconto de 10% você ira pagar R${:.2f}'.format(total))
elif opcao == 2:
  plano = int(input('Escolha o plano de pagamento:\n1: A vista\n2: 2 vezes\n3: 3 vezes\n'))
  if plano == 1:
    total = preco-(preco*0.05)
    print('Com o desconto de 5% você ira pagar R${:.2f}'.format(total))
  elif plano == 2:
    print('O valor que você irá pagar será R${}'.format(preco))
  elif plano == 3:
    total = preco +(preco*0.20)
    print('Com o juros de 20% você irá pagar R${}'.format(total))
else:
  print('Incorreto. Escolha uma das opção acima!')
print('Obrigado e boas compras')