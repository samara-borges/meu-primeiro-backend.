import random

print("--- BEM-VINDO AO JOGO DE ADIVINHAÇÃO ---")
numero_secreto = random.randint(1, 10) # Aumentamos o limite para 100!
pontos = 100

print("Escolha o nível de dificuldade:")
print("(1) Easy (2) Medium (3) Hard")

nivel = int(input("Define level: "))

if nivel == 1:
    tentativas = 10
elif nivel == 2:
    tentativas = 5
else:
    tentativas = 3
    # O código que você já tem continua aqui em cima...

while tentativas > 0:
    print(f"Você tem {tentativas} chances e {pontos} pontos.")
    chute = int(input("Qual o seu palpite? "))

    if chute == numero_secreto:
        print(f"✨ PARABÉNS! Você venceu com {pontos} pontos!")
        break
    else:
        tentativas = tentativas - 1
        # Perde 10 pontos a cada erro
        pontos = pontos - 10
        
        if tentativas > 0:
            print("Errou! Tente novamente.")
        else:
            print(f"Game Over! O número era {numero_secreto}.")