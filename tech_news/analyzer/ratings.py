from tech_news.database import db


# Requisito 10
def top_5_news():
    """
    Requisito 10 - Passos a se seguir:
    1 - A função vai listar as cinco notícias mais populares
    2 - Para calcular a popularidade, basta somar shares e comments
    3 - Fazer um sorte descendente da popularidade
    4 - No caso de empate, fazer um sorte ascendente de título
    5 - O retorno tem que ser um array de tuplas [(title, url)]
    6 - Retornar quantas notícias existirem, caso tenha menos que 5
    7 - Caso não seja encontrado, retornar uma lista vazia

    Lógica a se pensar:
    Voltando ao assunto aggregations:
    1 - Criar uma variável que vai receber um lista que passa por um pipeline
    2 - Contruir o pipeline da seguinte maneira:
        - criar um campo $addFields de popularidade
        - esse campo vai ser a soma $add de shares_count e comments_count
        - fazer um $sort de popularity (-1) e title (1)
        - fazer um $limit de 5
    3 - Percorrer essa lista e para cada item, recuperar os valores de
        título e url
    4 - retornar a lista com o tupla desses valores

    Para entender o assunto de aggregations, consultei a documentação:
    https://www.mongodb.com/docs/manual/reference/operator/aggregation-pipeline/
    """
    search_news = db.news.aggregate([
        {"$addFields": {
            "popularity": {
                "$add": ["$comments_count", "$shares_count"]
            }}},
        {"$sort": {"popularity": -1, "title": 1}},
        {"$limit": 5}
    ])
    list_top_5_news = []
    for news_dicts in search_news:
        list_top_5_news.append((news_dicts["title"], news_dicts["url"]))
    return list_top_5_news


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
