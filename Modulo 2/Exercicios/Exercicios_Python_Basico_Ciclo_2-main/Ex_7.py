# Crie uma lista com 3 dicionários, cada um representando uma pessoa (contendo nome, idade, cidade). Use um laço para imprimir o nome de cada pessoa.



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
pessoas = [
    {"nome": "Gustavo", "idade": 12, "cidade": "São Paulo"},
    {"nome": "Miguel", "idade": 18, "cidade": "Rio de Janeiro"},
    {"nome": "Kaio", "idade": 17, "cidade": "Belo Horizonte"}
]

# Laço para imprimir o nome de cada pessoa
for pessoa in pessoas:
    print(pessoa["nome"])
    