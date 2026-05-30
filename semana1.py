nome = "Carlos"
idade = 25
altura = 1.75
programador = True

idade = int(input("Qual a sua idade?"))
peso = float(input("Qual o seu peso?"))
altura = float(input("Qual sua altura?"))

imc = peso/(altura**2)

if imc < 18.5:
    classificacao = "abaixo do peso"
elif imc >= 18.5 and imc <= 24.9:
    classificacao = "peso normal"
elif imc >= 25 and imc <= 29.9:
    classificacao = "sobrepeso"
else:
    classificacao = "obesidade"
    

print(f" Seu imc {imc: .1f}, Você está com {classificacao}")

#print("Olá", nome + "! Você tem", str(idade), "anos.")
#print(f"Olá {nome}  ! Você tem {idade} anos.")
print(type(nome))
print(type(idade))
