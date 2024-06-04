i = int(input('Em qual número você quer começar a contagem? '))
f = int(input('Em qual número quer terminar a contagem? '))
p = int(input('Pulando quantos números? '))
for c in range(i,f,p):
  print(c)