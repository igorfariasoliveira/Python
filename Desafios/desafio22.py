nome = input("Qual o seu nome? ")
nome_sem_espaço = nome.replace(" ","")
nome_separado = nome.split(" ")
primeiro_nome = nome_separado[0]
print(nome.upper())
print(nome.lower())
print(len(nome_sem_espaço))
print(len(primeiro_nome))
