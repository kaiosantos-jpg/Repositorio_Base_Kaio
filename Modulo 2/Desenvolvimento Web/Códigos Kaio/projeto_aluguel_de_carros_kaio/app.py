# import streamlit as st

# ##aqui eu coloco o titulo
# st.title('Olá, devs!')

# ##digitando algo
#st.write('Eu adoro fazer programação em python com o professor Mateus!')

# #criando um calendario
# date = st.date_input("selecione uma data")

# ##permitindo o upload do aqruivo
# file = st.file_uploader("Pick a File")



#python -m streamlit run app.py
#write = escrever algo
#title = titulo
#date = inserir data
#file = inserir um arqvuivo

import streamlit as st
import pandas as pd

#sidebar

st.sidebar.image("logo.png")
st.sidebar.title('Kaio motors')

carros = ['Lamborghini', 'Uno', 'Ferrari', 'Camaro', 'Golf GTI', 'Palio', 's10', 'Siena', 'Porsche', 'BMW']

opcao = st.sidebar.selectbox('EScolha o carro que foi alugado', carros)

#Principal
st.title('Car Future - Aluguel de Carros')

st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias o {opcao} foi alugado?')
km = st.text_input(f'Quantos km você rodou com o {opcao}?')


###COpia aqui agora

if opcao == 'Lamborghini':
    diaria = 5500
    
elif opcao == 'Uno':
    diaria = 130
    
elif opcao == 'Ferrari':
    diaria = 3250
    
elif opcao == 'Camaro':
    diaria = 2000
    
elif opcao == 'Golf GTI':
    diaria = 1000
    
elif opcao =='Palio':
    diaria = 150
    
elif opcao == 's10':
    diaria = 1200
    
elif opcao == 'Siena':
    diaria = 120
    
elif opcao == 'Porsche':
    diaria = 3500
    
elif opcao == 'BMW':
    diaria = 538.90
    
    
    
    
if st.button('Calcular'):
    dias = int(dias)
    km = float(km)
    
    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias+total_km
    
    st.warning(f'Você alugou o {opcao} por {dias} dias e rodou {km}km. O valor total a pagar é R${aluguel_total:.2f}')
