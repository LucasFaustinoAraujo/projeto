import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

#configuração da pagina
st.set_page_config("Trabalho_IoT", page_icon=":tada:", layout="wide")

#tema do projeto
st.title("Tema do Projeto: Aplicativo de monitoramento de preços de jogos em diversas plataformas")
st.write("##")
st.write("##")
st.write("##")
left_column, right_column = st.columns(2)
with left_column:
# Alunos e orientador usando colunas
    st.header('Alunos:')
    st.write(
        """
        - Lucas Faustino Araújo
        - Matheus Sá Oliveira
        - Isaque Lopes Alves
        - Rennan Girão Alves
        """
        )
with right_column:
    st.header("Orientador:")
    st.write("- Rafael Teixeira de Araújo")
#espaço em branco
st.write("##")
st.write("##")
st.write("##")
#parte objetiva
st.subheader("Objetivo: Uma experiência diferente de como comprar jogos.")

