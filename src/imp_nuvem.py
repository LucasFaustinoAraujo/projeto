import requests
from bs4 import BeautifulSoup

def extrair_preco(preco_element):
    integer = preco_element.find('span', class_='integer')
    decimal = preco_element.find('span', class_='decimal')
    if integer and decimal:
        return f"R${integer.text}{decimal.text}"
    else:
        return "Preço não encontrado"

def retorna_preco(url):
    if url == "0":
        return "Este jogo não está disponível na plataforma."

    # Cabeçalhos (headers)
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    }

    #requisição HTTP com cabeçalhos
    response = requests.get(url, headers=headers)
    
    # Verifica a requisição 
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontra o preço final do produto
        game_price_element = soup.find('span', {'class': 'product-price--val'})
        game_price = extrair_preco(game_price_element)
        
        return game_price
    else:
        return "Erro ao acessar a página."