def ordenar_produtos(lista_produtos):
    # sort() modifica a lista original (Ordem Crescente)
    lista_produtos.sort(key=lambda x: x["preco"])
    
    # sorted() cria uma nova lista (Ordem Decrescente)
    lista_decrescente = sorted(lista_produtos, key=lambda x: x["preco"], reverse=True)
    
    return lista_produtos, lista_decrescente