import random

numero_secreto = random.randint(1, 10)
tentativas = 3

print("--- VOCÊ TEM 3 CHANCES ---")

while tentativas > 0:
    chute = int(input("Qual o seu palpite? "))
    
    if chute == numero_secreto:
        print("🏆 PARABÉNS! Você venceu a máquina!")
        break
    else:
        tentativas = tentativas - 1
        if tentativas > 0:
            print("Errou! Você ainda tem " + str(tentativas) + " chances.")
        else:
            print("Game Over! O número era " + str(numero_secreto))