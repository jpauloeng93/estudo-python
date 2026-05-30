def calcular_imc(peso, altura):
    
    imc = peso/(altura**2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        classificacao = "abaixo do peso"
    elif imc >= 18.5 and imc <= 24.9:
        classificacao = "peso normal"
    elif imc >= 25 and imc <= 29.9:
        classificacao = "sobrepeso"
    else:
        classificacao = "obesidade"

    return classificacao

def exibir_resultado(nome, imc, classificacao):
    print(f"Olá {nome}, seu imc {imc: .1f}, e você está com {classificacao}.")

nome = input("Qual o seu nome?")
peso = float(input("Qual o seu peso?"))
altura = float(input("Qual sua altura?"))

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)
exibir_resultado(nome, imc, classificacao)
    


#print("Olá", nome + "! Você tem", str(idade), "an