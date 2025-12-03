# Faça um código que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
# Exemplo de Resultado: O Seu salário atual é de R$1500,00 com o aumento de 15% seu novo salário será de R$1725,00
salario = float(input("Digite seu salário:"))
aumento = 15
salario_novo = salario + (salario * aumento / 100)

print(salario_novo)
