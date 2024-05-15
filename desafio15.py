dias = int(input("Quantos dias ficou com o carro? "))
quilomentros = float(input("Quantos quilometros rodou com ele? "))
precoaluguel = dias * 60
precodistancia = quilomentros * 0.15
totalapagar = precoaluguel + precodistancia
print('Você ira pagar o valor de {:.2f}R$'.format(totalapagar))