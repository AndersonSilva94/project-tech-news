"""
Requisito 12 - Passos a se seguir:
1 - Criar uma função que será um menu do programa
2 - o menu deve exibir exatamente o texto:
    Selecione uma das opções a seguir:
     0 - Popular o banco com notícias;
     1 - Buscar notícias por título;
     2 - Buscar notícias por data;
     3 - Buscar notícias por fonte;
     4 - Buscar notícias por categoria;
     5 - Listar top 5 notícias;
     6 - Listar top 5 categorias;
     7 - Sair.
3 - Caso a opção 0 seja selecionada - retornar "Digite quantas notícias serão buscadas:"
    - Caso seja o 1 - "Digite o título:"
    - Caso seja o 2 - "Digite a data no formato aaaa-mm-dd:"
    - Caso seja o 3 - "Digite a fonte:"
    - Caso seja o 4 - "Digite a categoria:"
4 - Caso não seja nenhuma dessas opções retornar "Opção inválida" com sys.stderr
5 - Usar o input para receber a entrada de dados da pessoa usuária

Lógica a se seguir:
1 - Criar os inputs com os valores que vão ser digitados com suas respectivas mensagens
    - um input que vai 'mostrar o menu' pro usuário com as opções
2 - para as mensagens que serão trazidas conforme a tecla apertada, posso criar um
    dict onde cada chave é a opção, e seu valor é o input com a mensagem
3 - fazer um try que será um print do dict na posição que a pessoa irá digitar
4 - caso a pessoa digite um valor inexistente, retornar um stderr.write("Opção inválida")

OBS: usei a documentação para ver qual o tipo de except seria levantado no erro:
https://docs.python.org/3/library/exceptions.html
"""
from sys import stderr


# Requisito 12
def analyzer_menu():
    menu_select_info = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por fonte;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.\n"
    )
    select_options = {
        "0": input("Digite quantas notícias serão buscadas:"),
        "1": input("Digite o título:"),
        "2": input("Digite a data no formato aaaa-mm-dd:"),
        "3": input("Digite a fonte:"),
        "4": input("Digite a categoria:")
    }
    try:
        print(select_options[menu_select_info])
    except KeyError:
        stderr.write("Opção inválida")
