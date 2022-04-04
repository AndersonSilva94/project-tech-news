from tech_news.database import search_news
from datetime import datetime


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
    """
    Requisito 7 - Passos a se seguir:
    1 - Buscar no banco de dados, notícias por data
    2 - O formato a ser considerado é aaaa-mm-dd
    3 - Retornar ao final uma lista de tuplas com as notícias
        encontradas da seguinte forma:
        [('titulo', 'url')]
    4 - Caso a data seja inválida ou em formato diferente, retornar
    um ValueError com a msg 'Data inválida'
    5 - Caso não seja encontrada, retornar uma lista vazia

    Lógica a se pensar:
    1- Verificar se a data é válida (usando try, except)
    2 - Criar uma variável que vai armazenar uma lista com os retornos da
        busca realizada
    3 - Para cada valor dessa lista, criar uma tupla de (title, url)
    4 - Adicionar cada tupla à uma nova lista, que inicialmente é vazia
    5 - retornar a lista

    OBS: para fazer a verificação da data, busquei no link:
    https://stackoverflow.com/questions/9978534/match-dates-using-python-regular-expressions/9978701
    """
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    data_results = search_news({
        "timestamp": {
            "$regex": date,
            "$options": "i"
        }
    })
    list_tuples = []
    for news_dict in data_results:
        list_tuples.append((news_dict["title"], news_dict["url"]))
    return list_tuples


# Requisito 8
def search_by_source(source):
    """
    Requisito 8 - Passos a se seguir:
    1 - Buscar no banco de dados, notícias por source
    2 - Segue os mesmos passos dos requisitos anteriores

    Lógica a se pensar:
    1- Segue a mesma linha de lógica de busca e retorno dos
    requisitos anteriores
    """
    data_results = search_news({
        "sources": {
            "$regex": source,
            "$options": "i"
        }
    })
    list_tuples = []
    for news_dict in data_results:
        list_tuples.append((news_dict["title"], news_dict["url"]))
    return list_tuples


# Requisito 9
def search_by_category(category):
    """
    Requisito 9 - Passos a se seguir:
    1 - Buscar no banco de dados, notícias por category
    2 - Segue os mesmos passos dos requisitos anteriores

    Lógica a se pensar:
    1- Segue a mesma linha de lógica de busca e retorno dos
    requisitos anteriores
    """
    data_results = search_news({
        "categories": {
            "$regex": category,
            "$options": "i"
        }
    })
    list_tuples = []
    for news_dict in data_results:
        list_tuples.append((news_dict["title"], news_dict["url"]))
    return list_tuples
