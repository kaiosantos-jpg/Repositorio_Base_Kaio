# Utilize um loop while e um loop for para adicionar itens na lista.
# Peça para que o usuário digite quantos filmes deseja adicionar, e também os nomes dos filmes



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

filmes = [] # Não apague esta lista

# LOOP WHILE
qtd = int(input("Quantos filmes deseja adicionar? "))
print("\nAdicionando com WHILE:")
i = 0
while i < qtd:
    nome = input(f"Digite o nome do {i+1}º filme: ")
    filmes.append(nome)
    i += 1
    
    print("\nLista de filmes adicionados (while):")
print(filmes)

# LOOP FOR
filmes = []  # Reiniciando a lista
print("\nAdicionando com FOR:")
for i in range(qtd):
    nome = input(f"Digite o nome do {i+1}º filme: ")
    filmes.append(nome)

print("\nLista de filmes adicionados (for):")
print(filmes)
