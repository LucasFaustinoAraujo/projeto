import requests
from bs4 import BeautifulSoup

def retorna_preco2(url):
    # Verifica se a URL é igual a 0
    if url == "0":
        return "Este jogo não está disponível na plataforma"

    # Envia uma solicitação GET para a página
    response = requests.get(url)

    # Verifica se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Analisar a página com BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Encontrar o elemento que contém o preço de promoção
        sale_price_element = soup.find("div", {"class": "game_purchase_price"})
        
        # Se o jogo estiver em promoção, obtenha o preço de promoção
        if sale_price_element:
            price = sale_price_element.get_text(strip=True)
            return price
        else:
            # Se o jogo não estiver em promoção, obtenha o preço normal
            price_element = soup.find("div", {"class": "discount_original_price"})

            if price_element:
                price = price_element.get_text(strip=True)
                return price
            else:
                return "Preço não encontrado"
    else:
        return -2
