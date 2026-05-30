contador =0

while contador < 5:
    print(contador)
    contador = contador + 1

for i in range(10):
    if i == 7:
        break
    elif i == 2:
        continue
    print(i)

import random

def verificar_numero(numero,numero_secreto):
    if numero == numero_secreto:
        return True
    elif numero < numero_secreto:
        print("Numero esta muito baixo, tente um numero maior")
        return False 
    else:
        print("Numero esta muito alto, tente um numero menor")
        return False

numero_secreto = random.randint(1, 100)
tentativas = 0
acertou = False

while not acertou:
    numero = int(input("Digite um número: "))
    tentativas += 1
    acertou = verificar_numero(numero,numero_secreto)

print(f"Você acertou o numero numero secreto {numero_secreto} em {tentativas} tentativas")
