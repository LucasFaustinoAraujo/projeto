import streamlit as st
import requests
from bs4 import BeautifulSoup
from src.imp_nuvem import retorna_preco
from src.imp_green import obter_preco_jogo
from src.imp_steam import retorna_preco2
#paginas nomeadas tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Fight Game", "RPG", "FPS", "Terror", "Plataforma"])

#FG
with tab1:
    st.header("Fight Games:boxing_glove:")

    #estrutura de colunas para posicionar as imagens ao lado
    col1, col2, col3 = st.columns(3)

    #coluna contendo: corpo, imagem, preço
    with col1:
        st.header("Mortal Kombat 1")
        st.image("https://sm.ign.com/t/ign_br/screenshot/default/mk-1-capa_puv2.1024.jpg", width=450)
        precon = retorna_preco("https://www.nuuvem.com/br-pt/item/mortal-kombat-1")
        st.write(f":white[Preço: {precon}]")
        precog = obter_preco_jogo("https://www.greenmangaming.com/pt/games/mortal-kombat-1-pc/")
        st.write(f":green[Preço: R$ {precog}]")
        precos = retorna_preco2("https://store.steampowered.com/app/1971870/Mortal_Kombat_1/")
        st.write(f":blue[Preço: {precos}]")
    #coluna contendo: corpo, imagem, preço
    with col2:
        st.header("Street Fighter V")
        st.image("https://image.api.playstation.com/cdn/UP0102/CUSA01200_00/nTW0mknYHcyGeTUGBwIsS2wrQY8i7CVd.png", width=450)
        precon = retorna_preco("https://www.nuuvem.com/br-pt/item/street-fighter-v")
        st.write(f":white[Preço: {precon}]")
        precog = obter_preco_jogo("https://www.greenmangaming.com/pt/games/street-fighter-v-champion-edition-pc/")
        st.write(f":green[Preço: R$ {precog}]")
        precos = retorna_preco2("https://store.steampowered.com/app/310950/Street_Fighter_V/")
        st.write(f":blue[Preço: {precos}]")
    #coluna contendo: corpo, imagem, preço
    with col3:
        st.header("Pocket Bravery")
        st.image("https://gamearena.gg/wp-content/uploads/2023/08/2x1_NSwitch_PocketBravery-1024x576.jpg", width=450)
        precon = retorna_preco("https://www.nuuvem.com/br-pt/item/pocket-bravery")
        st.write(f":white[Preço: {precon}]")
        precog = obter_preco_jogo("https://www.greenmangaming.com/pt/games/pocket-bravery-pc/")
        st.write(f":green[Preço: R$ {precog}]")
        precos = retorna_preco2("https://store.steampowered.com/app/1555150/Pocket_Bravery/")
        st.write(f":blue[Preço: {precos}]")
  
#RPG  
with tab2:
    st.header("RPG :shield::crossed_swords:")

    #estrutura de colunas para posicionar as imagens ao lado
    col1, col2, col3 = st.columns(3)

    #coluna contendo: corpo, imagem, preço
    with col1:
        st.header("Lords of the Fallen")
        st.image("https://image.api.playstation.com/vulcan/ap/rnd/202308/2307/5b5caedff1afc1f8e36bafb49abe2a55baf873e0fd84fcd8.png", width=450)
        precon = retorna_preco("https://www.nuuvem.com/br-pt/item/lords-of-the-fallen-remake")
        st.write(f":white[Preço: {precon}]")
        precog = obter_preco_jogo("https://www.greenmangaming.com/pt/games/lords-of-the-fallen-pc/")
        st.write(f":green[Preço: R$ {precog}]")
        precos = retorna_preco2("https://store.steampowered.com/app/1501750/Lords_of_the_Fallen/")
        st.write(f":blue[Preço: {precos}]")
    #coluna contendo: corpo, imagem, preço
    with col2:
        st.header("Dark Souls 3")
        st.image("https://image.api.playstation.com/cdn/UP0700/CUSA03388_00/v8JlD8KcQUtTqaLBmpFnj1ESRR5zMkLk.png", width=450)
        precon = retorna_preco("https://www.nuuvem.com/br-pt/item/dark-souls-iii")
        st.write(f":white[Preço: {precon}]")
        precog = obter_preco_jogo("0") 
        st.write(f":green[Preço: {precog}]")
        precos = retorna_preco2("https://store.steampowered.com/app/374320/DARK_SOULS_III/")
        st.write(f":blue[Preço: {precos}]")
    #coluna contendo: corpo, imagem, preço
    with col3:
        st.header("Elden Ring")
        st.image("https://mlx3nz5yukna.i.optimole.com/w:1024/h:1024/q:mauto/f:avif/https://lcgamesdigitais.com.br/wp-content/uploads/2022/10/elden_239519f1-93dd-4732-809f-0cd4228d1fc7.jpg", width=450)
        precon = retorna_preco("https://www.nuuvem.com/br-pt/item/elden-ring")
        st.write(f":white[Preço: {precon}]")
        precog = obter_preco_jogo("0")
        st.write(f":green[Preço: {precog}]")
        precos = retorna_preco2("https://store.steampowered.com/app/1245620/ELDEN_RING/")
        st.write(f":blue[Preço: {precos}]")

#FPS
with tab3:
    st.header("FPS :gun:")

    #estrutura de colunas para posicionar as imagens ao lado
    col1, col2, col3 = st.columns(3)

    #coluna contendo: corpo, imagem, preço
    with col1:
        st.header("Doom Eternal")
        st.image("https://image.api.playstation.com/vulcan/ap/rnd/202010/0114/ERNPc4gFqeRDG1tYQIfOKQtM.png", width=450)
        precon = retorna_preco("https://www.nuuvem.com/br-pt/item/doom-eternal")
        st.write(f":white[Preço: {precon}]")
        precog = obter_preco_jogo("https://www.greenmangaming.com/pt/games/doom-eternal-pc/")
        st.write(f":green[Preço: R$ {precog}]")
        precos = retorna_preco2("https://store.steampowered.com/app/782330/DOOM_Eternal/")
        st.write(f":blue[Preço: {precos}]")
    #coluna contendo: corpo, imagem, preço
    with col2:
        st.header("Payday 3")
        st.image("https://image.api.playstation.com/vulcan/ap/rnd/202305/2909/a1a027289fadb563ddc04c1a3ec0f2b7f4f9f8dd7fe378c2.png", width=450)
        precon = retorna_preco("https://www.nuuvem.com/br-pt/item/payday-3")
        st.write(f"Preço: {precon}")
        precog = obter_preco_jogo("0")
        st.write(f":green[Preço: {precog}]")
        precos = retorna_preco2("https://store.steampowered.com/app/1272080/PAYDAY_3/")
        st.write(f":blue[Preço: {precos}]")  
    #coluna contendo: corpo, imagem, preço
    with col3:
        st.header("Rainbow Six Siege")
        st.image("https://arenaesports.com.br/wp-content/uploads/2018/09/rainbow_six_siege_destacada-1024x576.jpg", width=600)
        precon = retorna_preco("https://www.nuuvem.com/br-pt/item/tom-clancy-s-rainbow-six-siege")
        st.write(f"Preço: {precon}")
        precog = obter_preco_jogo("https://www.greenmangaming.com/pt/games/tom-clancys-rainbow-six-siege-pc/")
        st.write(f":green[Preço: R$ {precog}]")
        precos = retorna_preco2("https://store.steampowered.com/app/359550/Tom_Clancys_Rainbow_Six_Siege/")
        st.write(f":blue[Preço: {precos}]")  

#Terror
with tab4:
    st.header("Terror :skull:")

    #estrutura de colunas para posicionar as imagens ao lado
    col1, col2, col3 = st.columns(3)

    #coluna contendo: corpo, imagem, preço
    with col1:
        st.header("Dredge")
        st.image("https://image.api.playstation.com/vulcan/ap/rnd/202301/1712/N67SrtQhAeoOQbSqku6vdpDM.png ", width=450)
        precon = retorna_preco("https://www.nuuvem.com/br-pt/item/dredge")
        st.write(f":white[Preço: {precon}]")
        precog = obter_preco_jogo("https://www.greenmangaming.com/pt/games/dredge-pc/")
        st.write(f":green[Preço: R$ {precog}]")
        precos = retorna_preco2("https://store.steampowered.com/app/1562430/DREDGE/")
        st.write(f":blue[Preço: {precos}]")
    with col1:
        st.header("The Last of Us Pt 1")
        st.image("https://image.api.playstation.com/vulcan/ap/rnd/202206/0720/eEczyEMDd2BLa3dtkGJVE9Id.png", width=450)
        precon = retorna_preco("https://www.nuuvem.com/br-pt/item/the-last-of-us-part-1")
        st.write(f":white[Preço: {precon}]")
        precog = obter_preco_jogo("https://www.greenmangaming.com/pt/games/the-last-of-us-part-i-pc/")
        st.write(f":green[Preço: R$ {precog}]")
        precos = retorna_preco2("https://store.steampowered.com/app/1888930/The_Last_of_Us_Part_I/")
        st.write(f":blue[Preço: {precos}]")
    #coluna contendo: corpo, imagem, preço
    with col2:
        st.header("Outlast 2")
        st.image("https://image.api.playstation.com/cdn/UP2113/CUSA06623_00/5vXtP0O5fmnnyrNnWAinTz57d04szG3b.png", width=450)
        precon = retorna_preco("0")
        st.write(f":white[Preço: {precon}]")
        precog = obter_preco_jogo("https://www.greenmangaming.com/pt/games/outlast-2-pc/")
        st.write(f":green[Preço: R$ {precog}]")
        precos = retorna_preco2("https://store.steampowered.com/app/414700/Outlast_2/")
        st.write(f":blue[Preço: {precos}]")
    with col2:
        st.header("Back 4 Blood")
        st.image("https://cdn2.steamgriddb.com/file/sgdb-cdn/icon/9649dec6196d730c5e024f204477d8d1.png", width=450)
        precon = retorna_preco("https://www.nuuvem.com/br-pt/item/back-4-blood")
        st.write(f":white[Preço: {precon}]")
        precog = obter_preco_jogo("https://www.greenmangaming.com/games/back-4-blood-pc/")
        st.write(f":green[Preço: R$ {precog}]")
        precos = retorna_preco2("https://store.steampowered.com/app/924970/Back_4_Blood/")
        st.write(f":blue[Preço: {precos}]")
    #coluna contendo: corpo, imagem, preço
    with col3:
        st.header("Little Nightmares 1")
        st.image("https://image.api.playstation.com/cdn/UP0700/CUSA05929_00/BCXhBnr9X5jjilzuc5tyv7GOcBukog6V.png", width=450)
        precon = retorna_preco("https://www.nuuvem.com/br-pt/item/little-nightmares")
        st.write(f":white[Preço: {precon}]")
        precog = obter_preco_jogo("0")
        st.write(f":green[Preço: {precog}]")
        precos = retorna_preco2("https://store.steampowered.com/app/424840/Little_Nightmares/")
        st.write(f":blue[Preço: {precos}]") 
    with col3:
        st.header("Evil Dead ")
        st.image("https://image.api.playstation.com/vulcan/ap/rnd/202303/2310/85256cc58bd13f05151178ae713cef442e712a9b2aa7322e.png", width=450)
        precon = retorna_preco("https://www.nuuvem.com/br-pt/item/evil-dead-the-game")
        st.write(f":white[Preço: {precon}]")
        precog = obter_preco_jogo("https://www.greenmangaming.com/games/evil-dead-the-game-pc/")
        st.write(f":green[Preço: R$ {precog}]")
        precos = retorna_preco2("0")
        st.write(f":blue[Preço: {precos}]") 
        
#Plataforma
with tab5:
    st.header("Plataforma :roller_coaster:")

    #estrutura de colunas para posicionar as imagens ao lado
    col1, col2, col3 = st.columns(3)

    #coluna contendo: corpo, imagem, preço
    with col1:
        st.header("OlliOlli World")
        st.image("https://image.api.playstation.com/vulcan/ap/rnd/202106/0321/aOY1Fb5Tcw3Zti8m3qfZeIDM.png", width=450)
        precon = retorna_preco("https://www.nuuvem.com/br-pt/item/olliolli-world")
        st.write(f":white[Preço: {precon}]")
        precog = obter_preco_jogo("https://www.greenmangaming.com/games/olliolli-world-pc/")
        st.write(f":green[Preço: R$ {precog}]")
        precos = retorna_preco2("https://store.steampowered.com/app/1190170/OlliOlli_World/")
        st.write(f":blue[Preço: {precos}]")
    with col1:
        st.header("Blasphemous II")
        st.image("https://image.api.playstation.com/vulcan/ap/rnd/202307/2609/5b7d787deb993232e95a008bed7081f9a824049554ad1bc4.png", width=450)
        precon = retorna_preco("https://www.nuuvem.com/br-pt/item/blasphemous-2")
        st.write(f":white[Preço: {precon}]")
        precog = obter_preco_jogo("https://www.greenmangaming.com/pt/games/blasphemous-2-pc/")
        st.write(f":green[Preço: R$ {precog}]")
        precos = retorna_preco2("https://store.steampowered.com/app/2114740/Blasphemous_2/")
        st.write(f":blue[Preço: {precos}]")
    #coluna contendo: corpo, imagem, preço
    with col2:
        st.header("Hell is Other Demons")
        st.image("https://f4.bcbits.com/img/a2076475867_10.jpg", width=450)
        precon = retorna_preco("https://www.nuuvem.com/br-pt/item/hell-is-other-demons")
        st.write(f":white[Preço: {precon}]")
        precog = obter_preco_jogo("0")
        st.write(f":green[Preço: {precog}]")
        precos = retorna_preco2("https://store.steampowered.com/app/595790/Hell_is_Other_Demons/")
        st.write(f":blue[Preço: {precos}]")
    with col2:
        st.header("Steel Rats")
        st.image("https://image.api.playstation.com/cdn/UP2081/CUSA09236_00/GCdDqYzXnTzzHz1RGWaSdR8Q8CoieoiU.png", width=450)
        precon = retorna_preco("https://www.nuuvem.com/br-pt/item/steel-rats")
        st.write(f":white[Preço: {precon}]")
        precog = obter_preco_jogo("0")
        st.write(f":green[Preço: {precog}]")
        precos = retorna_preco2("https://store.steampowered.com/app/619700/Steel_Rats/")
        st.write(f":blue[Preço: {precos}]")
    #coluna contendo: corpo, imagem, preço
    with col3:
        st.header("Celeste")
        st.image("https://image.api.playstation.com/cdn/UP2120/CUSA11302_00/qHx7zoFGNn6BUHUOk2jSfBck2Zzbjulw.png", width=450)
        precon = retorna_preco("0")
        st.write(f":white[Preço: {precon}]")
        precog = obter_preco_jogo("0")
        st.write(f":green[Preço: {precog}]")
        precos = retorna_preco2("https://store.steampowered.com/app/504230/Celeste/")
        st.write(f":blue[Preço: {precos}]")  
    with col3:
        st.header("Dead Cells")
        st.image("https://image.api.playstation.com/cdn/UP4016/CUSA11253_00/7HKh6rDoPOZgu5bKj5QZ6qXe7DjQlutY.png", width=450)
        precon = retorna_preco("https://www.nuuvem.com/br-pt/item/dead-cells")
        st.write(f":white[Preço: {precon}]")
        precog = obter_preco_jogo("0")
        st.write(f":green[Preço: {precog}]")
        precos = retorna_preco2("https://store.steampowered.com/app/588650/Dead_Cells/")
        st.write(f":blue[Preço: {precos}]")          
        