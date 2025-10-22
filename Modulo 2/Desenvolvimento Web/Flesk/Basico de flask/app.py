### IMPORTANDO "PARTES" DO FLASK
from flask import Flask, render_template,request


## Criando o APP e dizendo que ele está nesse arquivo com nome dele
app = Flask(__name__)



### Criando rotas

## / Significa principal onde o site vai de cara
@app.route('/')
def ola_mundo():
    return "Olá Mundo, estou com saudades do streamlit"

## Aqui vamos criar uma nova rota, dessa vez vai ser a /contato
@app.route('/contato')
def contato():
    return render_template ('contato.html')
## Sua vez crie uma nova rota dessa vez /hobbies, la coloque algo que você goste de fazer, exemplo : jogar bola
@app.route('/hobbies')
def hobbies():
    return render_template ('hobbies.html')
# lembre-se de criar um template chamado hobbies.html

## Executando o arquivo
if __name__ == '__main__':
    app.run(debug=True)