#cidade = str('SanTo da berra').strip()
#cidade_separada = cidade.split(' ')
#print ('santo' in cidade_separada[0].lower())
#print(cidade)
#print(cidade_separada)

#Forma reduzida:
cidade =  str(input('Informe a cidade: ')).strip()
print(cidade[:5].upper() == 'SANTOS')
