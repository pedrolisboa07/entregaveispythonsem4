
def exibir_relatorio(lista_crescente, lista_decrescente, filtrados, categorias, tupla_estat, limite):
    print("\n================ RELATÓRIO FINAL ================")
    
    print("\n--- Categorias Encontradas (Sem Duplicatas) ---")
    for cat in categorias:
        print(f"- {cat}")

    print("\n--- Estatísticas de Preço (Tupla) ---")
    print(f"Menor Preço: R$ {tupla_estat[0]:.2f}")
    print(f"Maior Preço: R$ {tupla_estat[1]:.2f}")
    print(f"Média dos Preços: R$ {tupla_estat[2]:.2f}")

    print(f"\n--- Produtos Acima de R$ {limite:.2f} ---")
    for p in filtrados:
        print(f"- {p['nome']}: R$ {p['preco']:.2f}")

    print("\n--- Produtos em Ordem Crescente ---")
    for p in lista_crescente:
        print(f"- {p['nome']}: R$ {p['preco']:.2f}")

    print("\n--- Produtos em Ordem Decrescente ---")
    for p in lista_decrescente:
        print(f"- {p['nome']}: R$ {p['preco']:.2f}")