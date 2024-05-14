objeto = input("Digite algo: ")
print("O tipo primitivo é ",type(objeto))
print("É um número? ",objeto.isnumeric())#Essa é outra forma de concaternar
print("É uma letra ou palavra? " + str(objeto.isalpha()))
print("É maiusculo? {}".format(objeto.isupper))