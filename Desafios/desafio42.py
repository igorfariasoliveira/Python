a = int(input('Digite um lado do triângulo '))
b = int(input('Digite outro lado do triângulo '))
c = int(input('Digite mais um lado do triângulo '))
if abs(b - c)<a<b+c and abs(a-c)<b<a+c and abs(a-b)<c<a+b:
  print('\033[32mEssas retas podem formar um triangulo!')
  if a == b == c:
    print('É um triângulo equilátero')
  elif a != b and b != c and a != c:
    print('É um triângulo escaleno')
  else:
    print('É um triângulo isoceles')
else:
  print('\033[31mEssas retas não podem formar um triangulo!')