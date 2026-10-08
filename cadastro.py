# cadastro.py
def cadastrar_produtos():
    lista_produtos = []
    print(" Cadastro de Produtos ")
    
    while True:
        nome = input("Digite o nome do produto (ou 'sair' para encerrar): ").strip()
        if nome.lower() == 'sair':
            break
        
        preco = float(input(f"Digite o preço de '{nome}': "))
        categoria = input(f"Digite a categoria de '{nome}': ").strip()
        
        lista_produtos.append({
            "nome": nome,
            "preco": preco,
            "categoria": categoria
        })
        
    return lista_produtos