import json

ARQUIVO = "produtos.json"

def carregar_lista_produtos():
    try:
        with open(ARQUIVO, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_produtos(produtos):
    with open(ARQUIVO, "w") as arquivo:
        json.dump(produtos, arquivo, indent=4)

def adicionar_produto(produtos, nome, quantidade, preco):
    produto = {"nome": nome, "quantidade": quantidade, "preco": preco}
    produtos.append(produto)
    salvar_produtos(produtos)
    print(f"produto {nome} adicionado!")

def listar_produtos(produtos):
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return
    for i, produto in enumerate(produtos):
        print(f"{i + 1}. {produto['nome']} — {produto['quantidade']} — {produto['preco']} ")

def remover_produto(produtos, nome):
    produtos = [c for c in produtos if c['nome'] != nome]
    salvar_produtos(produtos)
    print(f"produto {nome} removido!")
    return produtos

def atualizar_quantidade(produtos, nome, quantidade):
    for produto in produtos:
        if produto['nome'] == nome:
            produto['quantidade'] = quantidade
            salvar_produtos(produtos)
            print(f"produto {nome} quantidade atualizada!")
            return produtos  # já encontrou, encerra o loop

    print(f"produto '{nome}' não encontrado.")
    return produtos
    
def gerar_relatorio(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    valor_total = 0
    produto_mais_caro = None

    print("Relatório de Estoque:\n")

    for produto in produtos:
        valor_total += produto['preco'] * produto['quantidade']

        if produto_mais_caro is None or produto['preco'] > produto_mais_caro['preco']:
            produto_mais_caro = produto

        if produto['quantidade'] < 5:
            print(f"  ⚠ {produto['nome']} — estoque baixo ({produto['quantidade']} unidades)")

    print(f"\nValor total do estoque: R$ {valor_total:.2f}")
    print(f"Produto mais caro: {produto_mais_caro['nome']} (R$ {produto_mais_caro['preco']:.2f})")

produtos = carregar_lista_produtos()

while True:
   
    try:
        resposta = int(input("\n1 - Cadastrar produto\n2 - Listar todos os produtos\n3 - Remover produto\n4 - Atualizar Quantidade\n5 - Gerar Relatorio\n0 - sair\nSelecione uma opção para seguir: "))

        if resposta == 1:
            print("Registro de novo produto\n")
            nome = input("Digite o nome do produto: ")
            quantidade =  float(input("Digite o numero de quantidade: "))
            preco = float(input("Digite o preço do produto: "))
            adicionar_produto(produtos, nome, quantidade,preco)

        elif resposta == 2:
            listar_produtos(produtos)

        elif resposta == 3: 
            nome = input("\nDigite o nome do produto para ser removido:")
            produtos = remover_produto(produtos, nome)

        elif resposta == 4:
            nome = input("Digite o nome do produto que queres atualizar a quantidade: ")
            quantidade = float(input("Digite a nova quantidade: "))
            produtos = atualizar_quantidade(produtos,nome,quantidade)

        elif resposta == 5:
            gerar_relatorio(produtos)

        else:
            break
    except ValueError:
        print("Numero Digitado Inválido, Reiniciando Fluxo\n\n.")
        continue