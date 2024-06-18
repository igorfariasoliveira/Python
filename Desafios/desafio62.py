num= int(input("Digite quantos elementos da sequencia de Fibonacci você quer ver: "))
c = 1
na = 1
nb = 0
nc = 0
while c <= num:
  print(na)
  nb = na 
  na += nc
  nc = nb
  c+=1