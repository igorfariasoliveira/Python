salario = float(input("Informe o seu salário. "))
aumento = salario*0.15
valor_final = salario+aumento
print("O valor do seu novo salário será de R${:.2f}.\nHouve um aumento de R${:.2f}".format(valor_final,aumento))