# Faça um programa que leia um número inteiro qualquer
# e mostre na tela a sua tabuada
# Exemplo:
# Você digitou o número : 10
# --------------- Tabuada do 10 ------------------
# 10 X 0 = 0
# 10 X 1 = 10
# E assim sucessivamente....
numero_digitado = int(input("digite um numero inteiro:"))

for numero in range(11):
    resultado = numero_digitado * numero
    print(f"{numero_digitado} X {numero} = {resultado}")