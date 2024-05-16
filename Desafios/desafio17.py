from math import sqrt
co = float(input('Informe o cateto oposto do triângulo '))
ca = float(input('Informe o cateto adjascente do triângulo '))
h= sqrt(pow(co,2)+pow(ca,2))
print('A hipotenusa desse triângulo retangulo é {:.2f}'.format(h))
