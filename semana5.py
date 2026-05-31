#tuplas e sets
#tuplas sao dados imutaveis ou constantes
ponto = (10,20)
x,y = ponto
print(x)
print(y)

pessoa = {"nome": "Carlos", "idade": 25}

for chave, valor in pessoa.items():
    print(chave, valor)
#Set é uma coleção sem ordem e sem valores repetidos — perfeito para eliminar duplicatas:

numeros = {1, 2, 2, 3, 3, 3}
print(numeros)  # {1, 2, 3} — duplicatas removidas automaticamente

emails = ["a@a.com", "b@b.com", "a@a.com", "c@c.com"]
unicos = list(set(emails))
print(unicos)  # sem repetições

#Arquivos e JSON

# Escrevendo
with open("dados.txt", "w") as arquivo:
    arquivo.write("Olá, mundo!\n")
    arquivo.write("Segunda linha\n")

# Lendo
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

#modos de abertura
"w"  # write — cria ou sobrescreve
"r"  # read — lê (padrão)
"a"  # append — adiciona no final sem apagar o que já tem

#JSON é o formato padrão para salvar e trocar dados estruturados. É basicamente um dicionário Python salvo em arquivo:
import json

alunos = [
    {"nome": "Carlos", "media": 8.5},
    {"nome": "Ana", "media": 6.0},
    {"nome": "João", "media": 8.0}
]

# Salvando
with open("alunos.json", "w") as arquivo:
    json.dump(alunos, arquivo, indent=4)

try:
# Lendo
    with open("alunos.json", "r") as arquivo:
        dados = json.load(arquivo)
    
    print(dados)
except FileNotFoundError:
    print("Arquivo não encontrado, iniciando lista vazia.")
    dados = []