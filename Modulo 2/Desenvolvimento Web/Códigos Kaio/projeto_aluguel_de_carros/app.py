import streamlit as st

##aqui eu coloco o titulo
st.title('Olá, devs!')

##digitando algo
st.write('Eu adoro fazer programação em python com o professor Mateus!')

#criando um calendario
date = st.date_input("selecione uma data")

##permitindo o upload do aqruivo
file = st.file_uploader("Pick a File")



#python -m streamlit run app.py
#write = escrever algo
#title = titulo
#date = inserir data
#file = inserir um arqvuivo