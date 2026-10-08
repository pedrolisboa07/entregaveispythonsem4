# filtragem.py
def filtrar_por_preco(lista_produtos, limite_preco):
    produtos_filtrados = []
    for produto in lista_produtos:
        if produto["preco"] > limite_preco:
            produtos_filtrados.append(produto)
    return produtos_filtrados
