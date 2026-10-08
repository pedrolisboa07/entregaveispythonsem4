
def calcular_estatisticas(lista_produtos):
    precos = [p["preco"] for p in lista_produtos]
    
    menor_preco = min(precos)
    maior_preco = max(precos)
    media_precos = sum(precos) / len(precos)
    
    # Retorna uma tupla imutável
    return (menor_preco, maior_preco, media_precos)