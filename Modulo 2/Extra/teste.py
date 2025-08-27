
# CRIE 2 LISTAS, UMA COM O NOME DE "CARROS"(4 CARROS), SEGUNDA LISTA COM O NOME DE PREÇO ALUGUEL VAI TER OS VALORES DO ALUGUEL
#PEÇA AO USUARIO O NOME DO CARRO QUE ELE QUER ALUGAR E QUANTOS DIAS ELE QUER ALUGAR
#CALCULAR QUANTO ELE VAI GASTAR DE ALUGUEL


# Lista de carros e preços
carros = ["i30", "hb20s", "uno", "corolla"]
preco_aluguel = [80, 150, 50, 225]  # preço por dia

# Mostrando opções
print("Carros disponíveis para aluguel:")
for i in range(len(carros)):
    print(f"{i+1} - {carros[i]} (R${preco_aluguel[i]} por dia)")

# Entrada do usuário
carro_escolhido = input("Digite o nome do carro que deseja alugar: ")
dias = int(input("Quantos dias você quer alugar? "))

# Verificando se o carro existe e calculando valor
if carro_escolhido in carros:
    indice = carros.index(carro_escolhido)
    total = preco_aluguel[indice] * dias
    print(f"Você vai gastar R${total} para alugar o {carro_escolhido} por {dias} dias.")
else:
    print("Carro não encontrado.")
    
    