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

#sidebar
st.sidebar.image("spotify.png")
st.sidebar.title('Gêneros musicais e seus artistas')

generos = ["Rock", "Trap", "Funk"]
artistas_genero = {
    "Rock": ["Scorpions", "Avenged Sevenfold", "Black Sabbath", "Decalius","My chemical romance","acdc", "Slipknot", "System of a down"],
    "Trap": ["Matue", "Teto", "Wiu", "Alee"],
    "Funk": ["MC Ig", "MC Daleste", "MC Kevin", "MC pipokinha"]
}

genero_selecionado = st.sidebar.selectbox('Escolha seu gênero musical', generos)


#Principal
if genero_selecionado:
    artista_selecionado = st.sidebar.selectbox(
        "Selecione o artista:",
        artistas_genero[genero_selecionado]
    )


if genero_selecionado == "Rock" and artista_selecionado == "Scorpions":
    st.title("Scorpions\n")
    st.write("A banda Scorpions é um grupo de rock formado em 1965, na Alemanha, pelo guitarrista Rudolf Schenker. Tornou-se mundialmente conhecida por seu estilo que mistura hard rock, heavy metal e baladas românticas. A formação clássica contou com Klaus Meine (vocal), Rudolf Schenker (guitarra), Matthias Jabs (guitarra), Francis Buchholz (baixo) e Herman Rarebell (bateria).\n")
    st.video("https://youtu.be/7pOr3dBFAeY?si=siP5-98pRZl-NhNZ")
    st.link_button(url= "https://open.spotify.com/playlist/37i9dQZF1DZ06evO1cSzqU?si=e-plzjL4TCmkjfQekvJEUg",label= "Spotify")
    
elif genero_selecionado == "Rock" and artista_selecionado == "Avenged Sevenfold":
    st.title("Avenged Sevenfold\n")
    st.write("A banda Avenged Sevenfold (A7X) surgiu em 1999, na Califórnia (EUA). Mistura metalcore, heavy metal e hard rock, tornando-se um dos nomes mais influentes do metal atual. Ficou famosa com álbuns como City of Evil (2005) e Nightmare (2010). A morte do baterista The Rev, em 2009, marcou a história da banda, mas eles seguiram em frente e continuam ativos, conhecidos por shows enérgicos e grande versatilidade musical.\n")
    st.video("https://youtu.be/IHS3qJdxefY?si=gwlfYCtNlNzs4oJV")
    st.link_button(url= "https://open.spotify.com/playlist/37i9dQZF1DZ06evO09Ahq0?si=vesvcq5JT4apXgghjMpczA",label= "Spotify")
    
elif genero_selecionado == "Rock" and artista_selecionado == "Black Sabbath":
    st.title("Black Sabbath\n")
    st.write("O Black Sabbath, formado em 1968 na Inglaterra, é considerado o criador do heavy metal. Com Ozzy Osbourne nos vocais, destacou-se com álbuns como Paranoid (1970) e músicas como Iron Man e War Pigs. Mesmo com várias mudanças na formação, influenciou gerações e encerrou a carreira em 2017, deixando um legado eterno no rock e metal.\n")
    st.video("https://youtu.be/0lVdMbUx1_k?si=S9zYruk9ZN7pws-L")
    st.link_button(url= "https://open.spotify.com/playlist/37i9dQZF1DZ06evO3oYXfO?si=JbeVdwthQUGaxXaGMpAgDg",label= "Spotify")
    
elif genero_selecionado == "Rock" and artista_selecionado == "Decalius":
    st.title("Decalius\n")
    st.write("Decalius é um projeto solo de Depressive Black Metal, criado por Braulio Avelar Rodriguez em Seattle (EUA), entre 2016 e 2019. Suas músicas exploram temas de solidão, dor e depressão. Lançou álbuns como Isolated from Life (2021), Exiled in the Dark (2022) e Dehumanizing Loneliness (2023). Atualmente, o projeto está em pausa indefinida, mas deixou forte marca na cena underground do DSBM.\n")
    st.video("https://youtu.be/eIhANQNMsIk?si=CMJ6euscJNIGvtek")
    st.link_button(url= "https://open.spotify.com/playlist/37i9dQZF1DZ06evO0Mw4Jc?si=Bl2w0SJCQ0KKZWaG2Wt3dA",label= "Spotify")
    
elif genero_selecionado == "Rock" and artista_selecionado == "My chemical romance":
    st.title("My chemical romance\n")
    st.write("My Chemical Romance (MCR) é uma banda americana de rock alternativo/emo, formada em 2001 em Nova Jersey. Ficou famosa com álbuns como Three Cheers for Sweet Revenge (2004) e The Black Parade (2006), com hits como Helena e Welcome to the Black Parade. Separou-se em 2013, reuniu-se em 2019 e continua influente na cena alternativa.\n")
    st.video("https://youtu.be/UCCyoocDxBA?si=3nO_JMk_zb4V4YuS")
    st.link_button(url= "https://open.spotify.com/playlist/37i9dQZF1DZ06evO4xHh28?si=RxORLPIgSlG2zPRZH5p1Xw",label= "Spotify")
    
elif genero_selecionado == "Rock" and artista_selecionado == "acdc":
    st.title("ACDC\n")
    st.write("AC/DC é uma banda australiana de rock/hard rock, formada em 1973 por Malcolm e Angus Young. Famosa por álbuns como Highway to Hell e Back in Black e hits como Thunderstruck, permanece ativa e é uma das mais influentes bandas de rock da história.\n")
    st.video("https://youtu.be/l482T0yNkeo?si=lghTy_yikggR40qJ")
    st.link_button(url= "https://open.spotify.com/playlist/37i9dQZF1DZ06evO49hLQA?si=SEyZNsgzQ6KOCBrSDCHgzg",label= "Spotify")
    
    
elif genero_selecionado == "Rock" and artista_selecionado == "Slipknot":
    st.title("Slipknot\n")
    st.write("Slipknot é uma banda americana de heavy metal, formada em 1995 em Iowa. Conhecida por suas máscaras e shows intensos, ficou famosa com álbuns como Slipknot (1999) e Iowa (2001). Apesar de mudanças na formação, continua ativa e é referência no metal moderno\n")
    st.video("https://youtu.be/XEEasR7hVhA?si=2Gw9ublXPZtW_aWx")
    st.link_button(url= "https://open.spotify.com/playlist/37i9dQZF1DZ06evNZYGncI?si=l-IrfNBpS6SqZ_wmIEoXMg",label= "Spotify")
    
    
elif genero_selecionado == "Rock" and artista_selecionado == "System of a down":
    st.title("System of a down\n")
    st.write ("System of a Down (SOAD) é uma banda americana de metal alternativo, formada em 1994 em Los Angeles. Famosa por álbuns como Toxicity (2001) e Mezmerize (2005) e hits como Chop Suey! e B.Y.O.B., mistura metal pesado com influências armênias e letras políticas. Continua ativa e influente no metal alternativo.\n")
    st.video("https://youtu.be/DnGdoEa1tPg?si=qDS9Qw9whmM4gxvD")
    st.link_button(url= "https://open.spotify.com/playlist/37i9dQZF1DZ06evO34PI4g?si=uTu6P0cWTrWR3ZQJHkdlzg",label= "Spotify")

elif genero_selecionado == "Trap" and artista_selecionado == "Matue":
    st.title("Matue\n")
    st.write("Matuê (Matheus Brasileiro Aguiar), nascido em 1993 em Fortaleza, é um dos maiores nomes do trap brasileiro. Ganhou destaque com “Anos Luz” (2017) e consolidou o sucesso com o álbum “Máquina do Tempo” (2020). Fundador da gravadora 30PRAUM, é hoje um dos artistas mais influentes da cena do rap e trap no Brasil.\n")
    st.video("https://youtu.be/CUFMfGu1yQc?si=yI2d0nK17cYuVety")
    st.link_button(url= "https://open.spotify.com/playlist/37i9dQZF1DZ06evO3aogAV?si=_3EGwA37Sbem3tZLAxPL6g",label= "Spotify")
    
elif genero_selecionado == "Trap" and artista_selecionado == "Teto":
    st.title("Teto\n")
    st.write("Teto (Mateus Henrique), nascido em 2001 na Bahia, é um dos principais nomes do trap brasileiro. Assinou com a gravadora 30PRAUM e ganhou destaque com músicas como M4 e Mustang Preto. Suas letras falam de ambição, conquistas e vida urbana, consolidando-o como destaque da nova geração do trap no Brasil.\n")
    st.video("https://youtu.be/V9clMZHDZ0I?si=UPCUueJTAfAIzibx")
    st.link_button(url= "https://open.spotify.com/playlist/37i9dQZF1DZ06evO3CL3a0?si=0OM1lu_eT9eTM6nrlLhfQA",label= "Spotify")
    
elif genero_selecionado == "Trap" and artista_selecionado == "Wiu":
    st.title("Wiu\n")
    st.write("WIU (Vinicius William Sales de Lima), nascido em 2002 em Fortaleza, é um rapper brasileiro ligado ao trap, reggaeton e funk. Começou a carreira em 2017 e se destacou ao integrar a gravadora 30PRAUM. Lançou álbuns como Manual de Como Amar Errado (2022) e Vagabundo de Luxo (2024), com hits como Coração de Gelo e Vampiro, conquistando grande reconhecimento no cenário do trap nacional.\n")
    st.video("https://youtu.be/dOFKVu9XL3s?si=4zsMO4QRSrxnOqv3")
    st.link_button(url= "https://open.spotify.com/playlist/37i9dQZF1DZ06evO2cAFVL?si=2Xyxs2uyTPGnyEYykjqbkw",label= "Spotify")
    
elif genero_selecionado == "Trap" and artista_selecionado == "Alee":
    st.title("Alee\n")
    st.write("Alee (Alee Vieira), nascido em 2001 em Camaçari, Bahia, é um rapper brasileiro de trap, R&B e drill. Começou na cena do R&B e se destacou com participações na mixtape Jovens Pretos Milionários. Lançou álbuns como Dias Antes do Caos (2023) e Caos (2024), conquistando reconhecimento nacional e se firmando como uma das promessas do trap brasileiro.\n")
    st.video("https://youtu.be/9LOwIpjqN7Y?si=zVLVK5SLNUW1Wyca")
    st.link_button(url= "https://open.spotify.com/playlist/37i9dQZF1DZ06evO3NNKWn?si=MdFbSRSlRJG_9qHAfFrk1Q",label= "Spotify")
    
elif genero_selecionado == "Funk" and artista_selecionado == "MC Ig":
    st.title("MC Ig\n")
    st.write("MC IG (Guilherme Sérgio Ramos de Souza), nascido em 1997 na Zona Norte de São Paulo, é um cantor de funk paulista, rap e trap. Ganhou destaque com o single 3 Dias Virado e se consolidou com músicas como Let’s Go 4, ficando meses no topo do Spotify Brasil. Além da carreira musical, também atua como empresário e mantém forte conexão com seus fãs.\n")
    st.video("https://youtu.be/Ro1nho_O-kU?si=WsL2F697CT7jkTBa")
    st.link_button(url= "https://open.spotify.com/playlist/37i9dQZF1DZ06evO1nRZQG?si=UjqVTxx1TjyCD8jXQqKPTw",label= "Spotify")
    
elif genero_selecionado == "Funk" and artista_selecionado == "MC Daleste":
    st.title("MC Daleste\n")
    st.write("MC Daleste (Daniel Pellegrine, 1992–2013) foi um cantor de funk paulista conhecido por hits como Bonde dos Menor e Deusa da Ostentação. Ficou famoso no gênero ostentação, mas faleceu tragicamente aos 20 anos durante um show em Campinas. Seu legado permanece como um dos maiores nomes do funk paulista, e sua história foi retratada no documentário MC Daleste – Mataram o Pobre Loco.\n")
    st.video("https://youtu.be/bfu_WYsRMFs?si=uh-Zk51CnAumlsEM")
    st.link_button(url= "https://open.spotify.com/playlist/37i9dQZF1DZ06evO2vHzFK?si=egC6pAWmRDG9ulQMnQ5HDw",label= "Spotify")
    
elif genero_selecionado == "Funk" and artista_selecionado == "MC Kevin":
    st.title("MC Kevin\n")
    st.write("MC Kevin (Kevin Nascimento Bueno, 1998–2021) foi um cantor brasileiro de funk carioca, nascido em São Paulo. Ganhou destaque com músicas como Cavalo de Troia, Veracruz e Rabiola. Sua carreira foi marcada pelo sucesso nas plataformas digitais e por parcerias com outros artistas do funk. Kevin faleceu tragicamente aos 23 anos, mas deixou um legado significativo na cena do funk brasileiro, sendo lembrado por sua energia e carisma.\n")
    st.video("https://youtu.be/mpp18MorKOA?si=bU8SIuk-rIEFBgPO")
    st.link_button(url= "https://open.spotify.com/playlist/37i9dQZF1DZ06evO3bsPpY?si=xJYYT5zARfOrtImBWDzzTw",label= "Spotify")

elif genero_selecionado == "Funk" and artista_selecionado == "MC pipokinha":
    st.title("MC pipokinha\n")
    st.write("MC Pipokinha (Doroth Helena de Sousa Alves), nascida em 1998 em Santa Catarina, é cantora e influenciadora brasileira de funk ousadia. Ficou conhecida com músicas como Bota na Pipokinha e Eu Sou a Pipokinha, ganhando destaque no TikTok e Spotify. Em 2022, assinou com a produtora Novo Império e alcançou grande sucesso financeiro. Em 2025, anunciou aposentadoria da carreira musical.\n")
    st.video("https://youtu.be/yW5Z83OOIHA?si=JWZ6uIPQxJQSwyZt")
    st.link_button(url= "https://open.spotify.com/playlist/37i9dQZF1DZ06evO4vsGnT?si=TYz3hiYIT9eHVNpX1_vcXw",label= "Spotify")




