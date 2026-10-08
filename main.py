# main.py
from cadastro import cadastrar_produtos
from filtragem import filtrar_por_preco
from ordenar import ordenar_produtos
from categorias import obter_categorias_unicas
from estatisticas import calcular_estatisticas
from relatorio import exibir_relatorio

def fluxo_principal():
    # 1. Cadastro
    produtos = cadastrar_produtos()
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    # 2. Filtragem
    limite = float(input("\nDefina um preço limite para filtragem: "))
    filtrados = filtrar_por_preco(produtos, limite)

    # 3. Categorias Únicas
    categorias = obter_categorias_unicas(produtos)

    # 4. Estatísticas
    estatisticas = calcular_estatisticas(produtos)

    # 5. Ordenação
    lista_crescente, lista_decrescente = ordenar_produtos(produtos)

    # 6. Relatório Final
    exibir_relatorio(lista_crescente, lista_decrescente, filtrados, categorias, estatisticas, limite)

if __name__ == "__main__":
    fluxo_principal()
