nomes = ["Carlos", "Ana", "João"]
numeros = [10, 20, 30, 40]
misto = [1, "texto", True, 3.14]

print(nomes[0])
print(nomes[1])
print(nomes[2])

nomes.append("Maria")
nomes.remove("Ana")
nomes.pop(0)

print(len(nomes))
print("João" in nomes)

for nome in nomes:
    print(nome)

numeros = [1,2,3,4,5]
dobros = [n * 2 for n in numeros]
print(dobros)

pares = [n for n in numeros if n%2 ==0]
print(pares)

alunos = [
    {"nome": "Carlos", "nota": 8.5},
    {"nome": "Ana", "nota": 6.0},
    {"nome": "João", "nota": 4.5}
]

for aluno in alunos:
    print(aluno["nome"], aluno["nota"])



alunos = []

def media_turma():
    total = sum(aluno["media"] for aluno in alunos)
    return total / len(alunos)

def cadastrar_aluno(nome, nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    situacao = "aprovado" if media >= 7 else "reprovado"
    aluno = {
        "nome": nome,
        "media": media,
        "situacao": situacao
    }
    alunos.append(aluno)

def exibir_relatorio():
    for aluno in alunos:
        print(f"{aluno['nome']} — média {aluno['media']:.1f} — {aluno['situacao']}")
    print(f"A media da turma foi {media_turma():.1f}")
    reprovados = [a["nome"] for a in alunos if a["situacao"] == "reprovado"]
    print(f"Reprovados {', '.join(reprovados)}")

cadastro = True

while cadastro:
    resposta = input("Deseja Cadastrar um novo aluno? (s/n)")
    if resposta == "s":
        nome = input(f"digite o nome do aluno {len(alunos) + 1}: ")
        nota1 = float(input(f"digite a nota 1 do aluno {len(alunos) + 1}: "))
        nota2 = float(input(f"digite a nota 2 do aluno {len(alunos) + 1}: "))
        nota3 = float(input(f"digite a nota 3 do aluno {len(alunos) + 1}: "))
        cadastrar_aluno(nome,nota1,nota2,nota3)
    else:
        cadastro = False
        exibir_relatorio()

