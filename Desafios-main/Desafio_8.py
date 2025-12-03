# Na mesma linha dos exercicios anteriores crie uma função chamada pode_ver_filme que recebe a idade e a classificação indicativa do filme
# classificacao: 'L' (Livre), 'Maior de 12', 'Maior de 14', 'Maior 16', 'Maior 18'

#Exemplo:
# idade = 10
# classificacao = 'Maior de 12'
# resposta = "Não pode assitir o filme"

idade = int(input("Digite sua idade: "))
classificacao = input("Digite a classificação do filme: ")

def pode_ver_filme(idade, classificacao):

    if idade <= 10 and classificacao == 'livre':
        print("Pode assistir o filme")
        
    elif idade >= 12 and classificacao == 'maior de 12':
        print("Pode assistir o filme")
        
    elif idade >= 14 and classificacao == 'maior de 14':
        print("Pode assistir o filme")
        
    elif idade >= 16 and classificacao == 'maior de 16':
        print(" pode assistir o filme")
        
    elif idade >= 18 and classificacao == 'maior de 18':
        print("Pode assistir o filme")
        
    else:
        print("Não pode assistir o filme")
        
pode_ver_filme(idade , classificacao)
        

        

        

        


