nome = str(input('Escreva seu nome completo: ')).strip()
nome_separado = nome.split()
print("Seu primeiro nome é {}".format(nome_separado[0]))
print("Seu ultimo nome é {}".format(nome_separado[-1]))