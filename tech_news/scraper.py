import requests
import time
from parsel import Selector


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
    """
    Requisito 2 - passos a se seguir:
    1 - A função recebe uma string com o conteúdo HTML da página
    2 - A função deve fazer uma raspagem de dados do conteúdo
        recebido para criar uma lista com URL's de notícias
    3 - Retornar essa lista
    4 - Caso não encontre url, retornar uma lista vazia
    """
    selector_element = Selector(html_content)
    links = []
    for link in selector_element.css("h3.tec--card__title"):
        links.append(link.css("a.tec--card__title__link::attr(href)").get())
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    """
    Requisito 3 - passos a se seguir:
    1 - A função recebe uma string com o conteúdo HTML da página
    2 - A função deve fazer uma raspagem de dados para retornar
        a URL da próxima página
    3 - Retornar essa URL
    4 - Caso não encontre url, retornar None
    """
    selector_element = Selector(html_content)
    next_link = selector_element.css("a.tec--btn::attr(href)").get()
    if next_link:
        return next_link
    else:
        return None


# Requisito 4
def get_generic_infos_news(css_code, selector_element):
    """
    Criar uma função que recebe o mesmo parâmetro, e trabalham
    com a mesma lógica de retorno dos dados
    """
    return selector_element.css(css_code).get()


def scrape_noticia(html_content):
    """BOMBAAAA! Ôh Requisito pai d'égua
    Requisito 4 - Passos a se seguir:
    1 - A função recebe o conteúdo geral de uma página de notícias
    2 - Essa função deve percorrer o conteúdo, procurando informações
        que vão preencher um dicionário com os atributos:
        url, title, timestamp, writer, shares_count, comments_count, summary
        sources, categories
    3 - Alguns pontos:
        - caso o writer não seja encontrado, salvar como None
        - caso shares_count não seja encontrado, salvar como 0
    4 - retornar esse dict

    Lógica principal: criar funções que vão fazer as tratativas para
    retornar cada um dos retornos esperados
    """
    selector_element = Selector(html_content)
    url_value = get_generic_infos_news(
        "head link[rel=canonical]::attr(href)",
        selector_element
    )
    title_value = get_generic_infos_news(
        "h1.tec--article__header__title::text",
        selector_element
    )
    timestamp_value = get_generic_infos_news(
        "time#js-article-date::attr(datetime)",
        selector_element
    )
    data_news = {
        "url": url_value,
        "title": title_value,
        "timestamp": timestamp_value
    }
    return data_news


"""url_test = ("https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/"
            + "155000-musk-tesla-carros-totalmente-autonomos.htm")
print(scrape_noticia(fetch(url_test)))"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
