import json

ARQUIVO = "contatos.json"

def carregar_contatos():
    try:
        with open(ARQUIVO, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_contatos(contatos):
    with open(ARQUIVO, "w") as arquivo:
        json.dump(contatos, arquivo, indent=4)

def adicionar_contato(contatos, nome, telefone):
    contato = {"nome": nome, "telefone": telefone}
    contatos.append(contato)
    salvar_contatos(contatos)
    print(f"Contato {nome} adicionado!")

def listar_contatos(contatos):
    if len(contatos) == 0:
        print("Nenhum contato cadastrado.")
        return
    for i, contato in enumerate(contatos):
        print(f"{i + 1}. {contato['nome']} — {contato['telefone']}")

def remover_contato(contatos, nome):
    contatos = [c for c in contatos if c['nome'] != nome]
    salvar_contatos(contatos)
    print(f"Contato {nome} removido!")
    return contatos

contatos = carregar_contatos()

while True:
   
    try:
        resposta = int(input("\n1 - Adicionar Contato\n2 - Listar Contatos\n3 - Remover Contato\n0 - sair\nSelecione uma opção para seguir: "))
    except ValueError:
        print("Digite apenas números.")
        continue

    if resposta == 1:
        print("Registro de novo Contato\n")
        nome = input("Digite o nome do Contato: ")
        telefone = input("Digite o numero de telefone apenas numeros: ")
        adicionar_contato(contatos, nome, telefone)
    elif resposta == 2:
        listar_contatos(contatos)
    elif resposta == 3: 
        nome = input("\nDigite o nome do contato para ser removido:")
        print(contatos)
        contatos = remover_contato(contatos, nome)
    else:
        break