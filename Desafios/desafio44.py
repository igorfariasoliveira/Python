preco = float(input('Qual o valor do produto? '))
opcao = int(input("Selecione a opçao de pagamento:\n1: dinheiro ou cheque\n2: cartão de credito\n"))
if opcao == 1:
  total = preco-(preco*0.10)
  print('Com o desconto de 10% você ira pagar R${:.2f}'.format(total))
elif opcao == 2:
  plano = int(input('Escolha o plano de pagamento:\n1: A vista\n2: 2x n'))