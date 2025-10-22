# Dado o dicionário, exiba o nome de todas as chaves e os tipos dos valores de cada chave, como no exemplo abaixo:


# Chave: nome | Tipo: <class 'str'>
# Chave: idade | Tipo: <class 'int'>
# Chave: saldo | Tipo: <class 'float'>
# Chave: conta_ativa | Tipo: <class 'bool'>
# Chave: endereco | Tipo: <class 'dict'>
# Chave: data_ativacao_cancelamento | Tipo: <class 'list'>


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

dados = {
    'nome' : 'Kaio',
    'idade' : 17,
    'saldo' : 146948.75,
    'conta_ativa' : False,
    'endereco' : {'Rua':'Rua Vila Nova', 'Bairro': 'Chacara solar 3'},
    'data_ativacao_cancelamento' : ['10/12/1989', '05/06/2012']
}

for chave, valor in dados.items():
    print(f"# Chave: {chave} | Tipo: {type(valor)} | Valor: {valor}")