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

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    numero = int(input("Digite um número: "))
    tentativas += 1
    if numero == numero_secreto:
        break 
    elif numero < numero_secreto:
        print("Numero esta muito baixo, tente um numero maior")
    else:
        print("Numero esta muito alto, tente um numero menor")
        
print(f"Você acertou o numero numero secreto {numero_secreto} em {tentativas} tentativas")
