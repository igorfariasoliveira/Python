a = float(input("Qual a altura da parede em metros? "))
l = float(input("Qual a largura da parede em metros? "))
area = a*l
quantidade = area/2
print("A area dessa parede é {}m². \nConsiderando que cada litro de tinta pinta uma area de 2m², serão necessarios {} litros de tinta para pintar essa parede".format(area,quantidade))