objeto = input("Digite algo: ")
print(type(objeto))
print("É um número? " + str(objeto.isnumeric()))
print("É uma letra ou palavra? " + str(objeto.isalpha()))
print("É maiusculo? " + str(objeto.isupper()))