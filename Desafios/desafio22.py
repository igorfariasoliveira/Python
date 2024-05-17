nome = input("Qual o seu nome? ")
print(nome.upper())
print(nome.lower())

nome_sem_espaço = nome.replace(" ","")
print(len(nome_sem_espaço))

nome_separado = nome.split(" ")
primeiro_nome = nome_separado[0]
print(len(primeiro_nome))
