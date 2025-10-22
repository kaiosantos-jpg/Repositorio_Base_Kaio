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

st.sidebar.image("logo_logitech.png")
st.sidebar.title('Peripherals For You')

produtos = ['Teclado PRO X 60', 'Teclado G915 TKL', 'Teclado PRO X TKL', 'Teclado G715', 'Teclado G815', 'Teclado PRO', 'Mouse G305', 'Mouse PRO X SUPERLIGHT', 'Mouse G203', 'Mouse G502 X LIGHTSPEED' , 'Mouse G403 HERO', 'Logitech MOUSE PAD - Studio Series', 'MousePad G740', 'MousePad G440']

opcao = st.sidebar.selectbox('Escolha o produto que deseja comprar', produtos)

#Principal
st.title('Logitech Store')

st.image(f'{opcao}.png')
st.markdown(f'## Você está prestes a comprar o: {opcao}')
st.markdown('---')


# quantidade_comprada = st.text_input(f'Quantos produtos você deseja comprar?')



###COpia aqui agora

if opcao == 'Teclado PRO X 60':
    valor =1169.91
    st.link_button(url = "https://www.logitechstore.com.br/teclado-mecanico-gamer-sem-fio-logitech-g-pro-x-60-lightspeed-rosa-magenta/?&utm_source=dtx&utm_medium=referral&utm_campaign=fy25q1_logi_npi_dtx_npi_url_game_game-pc_pro-series_teclado&utm_term=site&utm_content=website-cta",label= "Comprar")
    
elif opcao == 'Teclado G915 TKL':
    valor =  1299.90
    st.link_button(url = "https://www.logitechstore.com.br/teclado-mecanico-sem-fio-de-baixo-perfil-rgb-para-jogos-logitech-g915-tkl-carbon-tactile-branco/",label= "Comprar")

elif opcao == 'Teclado PRO X TKL':
    valor = 1439.91
    st.link_button(url = "https://www.logitechstore.com.br/teclado-mecanico-gamer-com-fio-usb-logitech-g-pro-x-tkl-lightspeed-magenta-com-layout-americano/?&utm_source=referral&utm_medium=dtx&utm_campaign=fy24q4_logi_npi__game_game-pc_pro-series_teclado&utm_term=site&utm_content=website-cta", label = "Comprar")
    
elif opcao == 'Teclado G715':
    valor = 1259.91
    st.link_button(url = "https://www.logitechstore.com.br/teclado-mecanico-gamer-sem-fio-logitech-g715-rgb-lightsync-com-switch-gx-brown-tactile/", label= "Comprar")
    
elif opcao == 'Teclado G815':
    valor = 1099.90
    st.link_button(url = "https://www.logitechstore.com.br/teclado-mecanico-logitech-g-g815-tactile-branco/", label= "Comprar")
    
elif opcao == 'Teclado PRO':
    valor = 729.90
    st.link_button(url="https://www.logitechstore.com.br/teclado-mecanico-rgb-para-jogos-logitech-g-pro-gx-blue-clicky/",label="Comprar")
    
elif opcao == 'Mouse G305':
    valor = 369.90
    st.link_button(url="https://www.logitechstore.com.br/mouse-sem-fio-para-jogos-logitech-g305-lightspeed/",label="Comprar")
    
elif opcao == 'Mouse PRO X SUPERLIGHT':
    valor =  899.90
    st.link_button(url="https://www.logitechstore.com.br/mouse-sem-fio-para-jogos-logitech-g-pro-x-wireless-preto-1031/",label="Comprar")
    
elif opcao == 'Mouse G203':
    valor = 189.90
    st.link_button(url="https://www.logitechstore.com.br/mouse-otico-para-jogos-logitech-g203-lightsync-azul/",label="Comprar")
    
elif opcao == 'Mouse G502 X LIGHTSPEED':
    valor = 799.90
    st.link_button(url="https://www.logitechstore.com.br/mouse-gamer-sem-fio-logitech-g502-x-lightspeed-branco/",label="Comprar")
    
elif opcao == 'Mouse G403 HERO':
    valor = 299.90
    st.link_button(url="https://www.logitechstore.com.br/mouse-para-jogo-logitech-g403-hero/",label="Comprar")

elif opcao == 'Logitech MOUSE PAD - Studio Series':
    valor = 49.90
    st.link_button(url="https://www.logitechstore.com.br/mouse-pad-studio-series-grafite/",label="Comprar")
    
elif opcao == 'MousePad G740':
    valor = 290.31
    st.link_button(url="https://www.logitechstore.com.br/mousepad-gamer-de-tecido-logitech-g-g740-preto/?&utm_source=referral&utm_medium=dtx&utm_campaign=fy24q4_logi_aon__game_game-pc_gaming-core_mousepad&utm_term=site&utm_content=website-cta",label="Comprar")
    
elif opcao == 'MousePad G440':
    valor = 193.76
    st.link_button(url="https://www.logitechstore.com.br/mousepad-gamer-rigido-logitech-g-g440-preto/?&utm_source=referral&utm_medium=dtx&utm_campaign=fy24q4_logi_aon__game_game-pc_gaming-core_mousepad&utm_term=site&utm_content=website-cta",label="Comprar")
    
    
    
    
# if st.button('calcular'):
#     quantidade_comprada = int(quantidade_comprada)
#     valor_total = quantidade_comprada * valor
    
 
    
#     st.warning(f'Você comprou {quantidade_comprada} produtos {opcao} por :{valor_total:.2f}')
