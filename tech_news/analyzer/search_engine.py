from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """
    Requisito 6 - Passos a se seguir:
    1 - Buscar no banco de dados, notícias por título
    2 - A função recebe uma string como título de notícia
    3 - Retornar ao final uma lista de tuplas com as notícias
        encontradas da seguinte forma:
        [('titulo', 'url')]
    4 - A busca deve ser case insensitive
    5 - Caso não seja encontrada, retornar uma lista vazia

    Lógica a se pensar:
    1 - Criar uma variável que vai armazenar uma lista com os retornos da
        busca realizada
    2 - Para cada valor dessa lista, criar uma tupla de (title, url)
    3 - Adicionar cada tupla à uma nova lista, que inicialmente é vazia
    4 - retornar a lista

    OBS: para fazer a busca em case insensitive busquei no link:
    https://www.mongodb.com/community/forums/t/case-insensitive-search-with-regex/120598/8
    """
    data_results = search_news({
        "title": {
            "$regex": title,
            "$options": "i"
        }
    })
    list_tuples = []
    for news_dict in data_results:
        list_tuples.append((news_dict["title"], news_dict["url"]))
    return list_tuples


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
