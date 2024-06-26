n = c = soma= 0
while True:
  n = int(input('Digite um número (999 para parar e somar): '))
  c+=1
  soma += n
  if n == 999:
    break
print(f"Você digitou {c} números. A soma ")