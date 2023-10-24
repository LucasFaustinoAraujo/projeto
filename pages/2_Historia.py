from PIL import Image
import streamlit as st

#imagens
img_contact_form = Image.open("images/imagem_trabalho.png")
img_contact_form2 = Image.open("images/super-mario-bros.png")
img_contact_form4 = Image.open("images/gd.png")

# Espaço
st.write("##")

#pergunta para publico
st.header('E a duvida é: :red[Jogos caros compensam?] :game_die: ')
with st.container():
    st.write("##")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form4)    
    with text_column:
        st.subheader('A resposta é: :green[depende],Gamers compram jogos o tempo todo, é um tipo de oferta e demanda, e com isso o mercado sempre está revolucionando.')

st.write("---")
# desenvolvimento
st.subheader("Os jogos evoluíram significativamente ao longo das décadas. Graficamente, passamos de gráficos 8 bits para visuais realistas em 3D, proporcionando uma experiência imersiva. Quanto à jogabilidade, os jogos evoluíram de mecânicas simples para experiências complexas, com narrativas ricas e multiplayer online. A introdução de realidade virtual e aumentada também expandiu as possibilidades. Em resumo, a evolução dos jogos trouxe avanços notáveis em gráficos, interatividade e acessibilidade, transformando a indústria do entretenimento.")

st.write("---")
#container e texto explicativo
with st.container():
    st.write("##")
    text_column, image_column = st.columns((1, 2))
    with text_column:
        st.subheader("""
        Desde nosso querido Super mario bros, até qualquer jogo atualmente, tem que ser fornecido um valor para a construção, funcionarios, devs, entre outros, para pelo menos ter um projeto, desde o enredo até a finalização.
                     
                     """)
    with image_column:
        st.image(img_contact_form2, width=650)  

st.write("---")
#container e pontos referencia dos valores jogos.
with st.container():
    st.write("##")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)    
    with text_column:
        st.header("E tem seus pontos negativos.")
        st.write("""
                     
                    - Barreiras financeiras: Os preços altos dos jogos podem tornar difícil para muitas pessoas, especialmente aqueles com orçamentos limitados, comprar os jogos que desejam.
                    - Exclusão social: Jogadores que não podem pagar os jogos mais caros podem se sentir excluídos de comunidades de jogos e conteúdo exclusivo.
                    - Falta de diversidade de jogadores: Os preços altos podem limitar a diversidade no público de jogadores, tornando os jogos inacessíveis para muitas pessoas.
                    - Jogos incompletos: Algumas empresas adotam a estratégia de lançar jogos base, conhecido como Standard, o que pode fazer com que os jogos básicos pareçam incompletos.
                    
                     """)

#container 
with st.container():
    st.write("##")
    st.write("##")
    st.subheader("""
        :smile: Seguindo para a aba Games, verá alguns dos jogos, e parâmetros para melhor informação.
                     
                     """)