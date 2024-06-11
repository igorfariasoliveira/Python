frase = str(input("Escreva uma pequena frase: ")).replace(' ','').upper()
inverso = ''
for letra in range(len(frase) -1, -1, -1):
  inverso += frase[letra]
if inverso == frase:
  print('Essa frase é um palindromo!')
else:
  print('Essa frase não é um palindromo')