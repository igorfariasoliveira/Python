preco=float(input("Digite o preço do produto. "))
des = preco*0.05
res = preco-des
print("O valor do seu desconto foi de R${:.2f}. \nO produto vai ficar por R${:.2f}".format(des,res))