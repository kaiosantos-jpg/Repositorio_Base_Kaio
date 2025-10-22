import streamlit as st


st.title("Calcula média")



nota1 = st.text_input("Digite sua primeira nota: ")
nota2 = st.text_input("Digite sua segunda nota: ")
nota3 =st.text_input("Digite sua terceira nota: ")
nota4 =st.text_input("Digite sua quarta nota: ")



if st.button("Calcula Média"):
    nota_1 = float(nota1)
    nota_2 = float(nota2) 
    nota_3 = float(nota3) 
    nota_4 = float(nota4)

    media = (nota_1 + nota_2 + nota_3 + nota_4)/4

    if media >= 7.0:
        st.warning(f"Sua média é {media:.2f}, parabens você está aprovado!✅")
        
    elif media >=5.0 and media < 7.0:
        st.warning(f"Sua média é {media:.2f}, cuidado, você está de recuperação⚠️")
        
    elif media <5.0:
        st.warning(f"Sua média é {media:.2f}, você está de reprovado!❌")
    