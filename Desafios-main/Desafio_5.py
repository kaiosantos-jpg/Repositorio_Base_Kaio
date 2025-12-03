# Agora vamos dar uma relembrada na aula de funções, pegue o código do exercicio anterior e transfome numa função,
# essa função deve receber uma lista e dessa lista escolher algum nome e dar um print
# ou seja vocês vão precisar criar a função e depois "chamar" a mesma para que ela execute.

from random import choice
nomes = ["Miguel", "Kaio", "Leonardo", "Gustavo A"]
alunos = ["Miguel", "Miguel", "Miguel", "Miguel"]

def ajuderian(lista):
    escolhido = choice(lista)
    print(f" O aluno que foi escolhido para ajudar o rian foi:{escolhido}, boa sorte!🤣🤣🤣🤣🤣🤣🤣🤣")
    

ajuderian(nomes)
    
    
ajuderian(alunos)
