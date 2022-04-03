import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
def get_generic_infos_news(css_code, selector_element, variable):
    """
    Criar uma função que recebe o mesmo parâmetro, e trabalham
    com a mesma lógica de retorno dos dados
    """
    if variable == "summary_value":
        result = selector_element.css(css_code).getall()
    else:
        result = selector_element.css(css_code).get()
    return result


def get_writer_news(selector_element):
    """
    Criar a função que vai buscar o nome do autor e caso não encontre
    retornar None
    """
    writer_value = selector_element.css("p.z--font-bold *::text").get()
    if writer_value is None:
        return selector_element.css("div.tec--timestamp__item a::text").get()
    else:
        return writer_value


def get_numbers_info_news(css_code, selector_element):
    """
    Criar uma função que vai pegar os valores de compartilhamento
    e comentários e retornar seus números, caso não exista valor
    retornar 0
    """
    number_value = selector_element.css(css_code).get()
    if number_value:
        return int(number_value.strip().split(" ")[0])
    else:
        return 0


def get_list_info_news(css_code, selector_element):
    """
    Criar uma função que vai tratar valores de lista para serem retornados
    """
    result = selector_element.css(css_code).getall()
    list_result = [element.strip() for element in result]
    return list_result


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
        selector_element,
        "url_value"
    )
    title_value = get_generic_infos_news(
        "h1.tec--article__header__title::text",
        selector_element,
        "title_value"
    )
    timestamp_value = get_generic_infos_news(
        "time#js-article-date::attr(datetime)",
        selector_element,
        "timestamp_value"
    )
    writer_value = get_writer_news(
        selector_element
    ).strip()
    shares_value = get_numbers_info_news(
        "nav.tec--toolbar > div:first-child::text",
        selector_element
    )
    comments_value = get_numbers_info_news(
        "button#js-comments-btn::attr(data-count)",
        selector_element
    )
    summary_value = "".join(get_generic_infos_news(
        "div.tec--article__body > p:nth-child(1) ::text",
        selector_element,
        "summary_value"
    ))
    sources_value = get_list_info_news(
        "div.z--mb-16 div a::text",
        selector_element
    )
    categories_value = get_list_info_news(
        "div#js-categories a::text",
        selector_element
    )
    data_news = {
        "url": url_value,
        "title": title_value,
        "timestamp": timestamp_value,
        "writer": writer_value,
        "shares_count": shares_value,
        "comments_count": comments_value,
        "summary": summary_value,
        "sources": sources_value,
        "categories": categories_value
    }
    return data_news


"""
url_test = ("https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/"
            + "155000-musk-tesla-carros-totalmente-autonomos.htm")
print(scrape_noticia(fetch(url_test)))
"""


# Requisito 5
def get_tech_news(amount):
    """
    Requisito 5 - Passos a se seguir:
    1 - A função recebe um parâmetro que é utilizado para buscar a quantidade
        exatas de notícias que foi passado
    2 - Utilizar as funções anteriores para criar a lógica de buscar e
        processar o conteúdo.
    3 - Salvar as notícias no mongodb e retorná-las logo após

    Lógica a se pensar:
    1 - fazer o fecth da url e salvar numa variável
    2 - percorrer essa variável enquanto ela for menor que amount
    3 - armazenar em uma variável o valor da próxima página
    4 - fazer o fetch formatado dessa url armazenada anteriormente
    5 - juntar à lista de urls, cada link de notícia
    6 - para cada item da lista de urls, limitando a quantidade passada
        - fazer uma requisição da página
        - adicionar à nova lista (de dados gerais) cada um dos valores
        trazidos anteriormente
    7 - salvar essa lista no banco de dados
    8 - retornar a lista
    """
    url = "https://www.tecmundo.com.br/novidades"
    html_content = fetch(url)
    list_news = scrape_novidades(html_content)
    new_list_news = []

    while len(list_news) < amount:
        next_page = scrape_next_page_link(html_content)
        next_page_content = fetch(next_page)
        for news_url in scrape_novidades(next_page_content):
            list_news.append(news_url)

    for link_news in range(amount):
        news_content = fetch(list_news[link_news])
        new_list_news.append(scrape_noticia(news_content))

    create_news(new_list_news)
    return new_list_news
