import requests
import time


# Requisito 1
def fetch(url):
    """
    Requisito 1 - passos a se seguir:
    1 - A função recebe uma url como parâmetro
    2 - Fazer uma requisição HTTP get utilizando o requests.get
    3 - Fazer um Rate Limit de 1 req/seg. (Ex: utilizar o time.sleep()
    4 - Caso a req retorne status 200, pegar o conteúdo de texto
    5 - Caso retorne um status diferente, retornar None
    6 - Caso não tenha resposta em até 3seg, a função é abandonada (Timeout)
        - retornar None
    """
    time.sleep(1)
    try:
        response_data = requests.get(url)
        if response_data.status_code != 200:
            return None
        else:
            return response_data.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
