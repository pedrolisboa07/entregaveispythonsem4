def obter_categorias_unicas(lista_produtos):
    categorias_lista = [p["categoria"] for p in lista_produtos]
    return set(categorias_lista)