import requests
from bs4 import BeautifulSoup
import re

def obter_preco_jogo(url):
    if url == "0":
        return "Este jogo não está disponível na plataforma."
    
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        price_element = soup.find('div', {'class': "prices-info"})

        if price_element:
            #expressão regular para extrair o preço
            price_text = price_element.text
            price_match = re.search(r"R\$\s*([\d,]+)", price_text)
            if price_match:
                game_price = price_match.group(1)
                return game_price
            else:
                return "Preço não encontrado"
        else:
            return "Preço indisponível"
    else:
        return "Erro"