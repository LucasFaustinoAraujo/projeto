import streamlit as st

# Explicação do que foi usado
left_column, right_column = st.columns(2)
with left_column:
    st.header('tecnologias que foram utilizadas')
    st.write("""
        No projeto em questão, utilizamos uma variedade de tecnologias para criar soluções interativas e eficazes. A principal linguagem de programação que adotamos foi o Python.

    Além disso, contamos com bibliotecas poderosas, como o Streamlit e o Pillow, que nos permitiram desenvolver aplicativos da web e realizar o processamento de imagens.

    Por fim, exploramos a técnica de web scraping, que nos possibilitou extrair informações valiosas de sites da internet de forma automatizada.

    Essas tecnologias, em conjunto, nos permitiram desenvolver soluções personalizadas, interativas e eficazes, tornando o projeto uma experiência recompensadora e produtiva. Se você tiver alguma curiosidade ou desejar saber mais sobre alguma dessas ferramentas, fique à vontade para explorá-las com mais profundidade na caixa de explicação.
             """)
with right_column:
    
    with st.expander("Python"):
        st.write("""
        É uma linguagem de programação de alto nível amplamente utilizada, conhecida por sua simplicidade e legibilidade. Foi criada por Guido van Rossum e lançada pela primeira vez em 1991. Uma das principais razões para a popularidade do Python é sua facilidade de aprendizado, o que o torna uma excelente escolha para iniciantes em programação.

    Python é uma linguagem interpretada, o que significa que você pode escrever e executar código diretamente, sem a necessidade de compilar o programa. Isso torna o desenvolvimento mais rápido e eficiente.

    Uma das características distintivas do Python é sua sintaxe limpa e fácil de ler, que se baseia no uso de espaços em branco para definir a estrutura do código, em vez de chaves ou delimitadores. Isso encoraja a escrita de código organizado e legível.

    Python é uma linguagem versátil, utilizada em uma ampla gama de aplicações, desde desenvolvimento web e automação de tarefas até análise de dados e aprendizado de máquina. Uma grande comunidade de desenvolvedores contribui para uma vasta coleção de bibliotecas e frameworks que tornam possível realizar uma variedade de projetos.

    Seja você um iniciante ou um programador experiente, Python é uma excelente escolha para começar a explorar o mundo da programação de computadores devido à sua simplicidade e poder. Portanto, não importa se você deseja criar um site, automatizar tarefas do dia a dia ou trabalhar em projetos complexos de ciência de dados, Python é uma linguagem que vale a pena aprender.
        """)
        
    with st.expander("Streamlit"):
        st.write("""
        É uma ferramenta que ajuda as pessoas que sabem programar em Python a criar sites e aplicativos simples. Com ela, você pode mostrar gráficos e dados de uma forma bonita e interativa, como um painel de controle.

    A coisa legal é que você não precisa se preocupar com coisas difíceis, como configurar servidores ou aprender linguagens de programação complicadas. Basta escrever o que deseja mostrar em Python, e o Streamlit cuida de todo o resto.

    Com o Streamlit, você pode criar visualizações de dados, aplicativos interativos e até mesmo fazer protótipos de ideias rapidamente. É ótimo para cientistas de dados e pessoas que desejam mostrar informações de maneira fácil e elegante na web. E, quando terminar, você pode compartilhar seu site ou aplicativo com outras pessoas apenas enviando o link.
        """)
        
    with st.expander("Pillow"):
        st.write("""
        É uma ferramenta que ajuda você a trabalhar com imagens no seu computador, como editar fotos ou criar imagens do zero. É como um programa para brincar com imagens, mas no seu próprio código.

    Com o Pillow, você pode redimensionar fotos, adicionar texto nelas, cortar partes indesejadas e até mesmo criar desenhos simples. É uma maneira divertida de mexer com imagens usando Python, a linguagem de programação que o Pillow entende.

    Então, se você gosta de editar fotos ou quer fazer algumas coisas legais com imagens no seu computador, o Pillow é um bom começo. É fácil de aprender e pode ser usado para muitas coisas divertidas com imagens.
           Vale dizer que esse pacote oferece suporte para variados formatos, como: JPEG, GIF, PNG, PDF, PCX, PSD, ICO, BMP, entre outros.
        """)
        
    with st.expander("Web Scraping"):
        st.write("""
        É como ter um robô que pega informações úteis em sites na internet, como preços de produtos, notícias ou qualquer coisa que você queira. É como ter um assistente que coleta dados para você.

    Imagine que você quer saber os preços dos seus jogos de vídeo favoritos em diferentes lojas online. Em vez de verificar manualmente cada site, um programa de web scraping pode fazer isso para você. Ele visita os sites, encontra os preços e organiza as informações em um lugar só, como uma lista.

    Então, se você precisa de informações da internet, o web scraping pode ser muito útil. Pode poupar tempo e trabalho, especialmente quando você precisa de informações de muitos lugares diferentes na web. É como ter um ajudante que reúne todas as informações importantes para você.
        """)
        
    with st.expander("Beautiful Soup"):
        st.write("""  
        É como uma ferramenta de busca para a internet. Imagine que a internet é um grande livro cheio de informações, e você quer encontrar coisas específicas, como receitas ou notícias.

O Beautiful Soup ajuda a encontrar essas informações. Ele "lê" as páginas da web, como se estivesse lendo um livro, e encontra as partes que você deseja, como títulos de notícias ou ingredientes de uma receita.

Em outras palavras, o Beautiful Soup é como um assistente que ajuda você a pegar pedaços de informações interessantes em páginas da web bagunçadas. É muito útil para extrair dados que você precisa, como encontrar o horário de um filme no cinema ou a previsão do tempo em um site. É uma ferramenta simples, mas poderosa, para coletar informações da internet de forma organizada.
        """)