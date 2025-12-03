# Crie uma função que calcule o valor da gorjeta de um garçom, baseada na qualidade do serviço
# qualidade_servico: 'ruim', 'medio', 'bom', 'excelente'

# A função deve pedir o valor da conta e a qualidade do serviço
# Se a qualidade for ruim a gorjeta é 0
# Se a qualidade for media a gorjeta é %2.5 do valor da conta
#Se a qualidade for bom a gorjeta é %4 do valor da conta
#Se a qualidade for excelente a gorjeta é %5 do valor da conta

#Exemplo:
# valor_conta = 100
# qualidade_servico = 'excelente'
# o valor da gorjeta é de R$ 5,00
valor_da_conta = float(input("Digite o valor da conta: "))
qualidade = input("Qual foi a qualidade do serviço: ")

def calcular(valor_da_conta, qualidade):

    if qualidade == 'ruim':
        gorjeta = 0
        print(f"Sua gorjeta é {gorjeta}")
        
    elif qualidade == 'medio':
        gorjeta = valor_da_conta * 0.025
        print(f"Sua gorjeta é  {gorjeta}")
        
    elif qualidade == 'bom':
        gorjeta = valor_da_conta * 0.04
        print(f"Sua gorjeta é  {gorjeta}")
        
    elif qualidade == 'excelente':
        gorjeta = valor_da_conta * 0.05
        print(f"Sua gorjeta é  {gorjeta}")
        
        
calcular(valor_da_conta, qualidade)