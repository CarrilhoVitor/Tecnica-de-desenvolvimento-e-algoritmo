import random
import time
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def linha():
    print("🕸️" * 40)

def adivinha_doces():
    limpar_tela()
    linha()
    print("🍬  ADIVINHA DOS DOCES MÁGICOS  🍬")
    linha()
    print("\nUma bruxa escondeu doces em um caldeirão encantado...\n")

    nivel = input("Escolha a dificuldade (fácil / médio / difícil): ").lower()
    if nivel == "facil":
        limite, tentativas = 20, 6
    elif nivel == "medio":
        limite, tentativas = 40, 5
    else:
        limite, tentativas = 80, 4

    numero_secreto = random.randint(1, limite)
    print(f"\nA bruxa cochicha: 'Há entre 1 e {limite} doces...'")

    while tentativas > 0:
        try:
            palpite = int(input(f"\nVocê tem {tentativas} tentativas. Adivinhe: "))
        except ValueError:
            print("Digite um número válido!")
            continue

        if palpite == numero_secreto:
            print("\n✨ CORRETO! Você ganhou todos os doces! 🍭✨")
            break
        elif palpite < numero_secreto:
            print("🔮 A bruxa ri: 'Mais... mais doces que isso!'")
        else:
            print("💀 Ela sussurra: 'Menos... você exagerou!'")

        tentativas -= 1
        time.sleep(1)

    if tentativas == 0 and palpite != numero_secreto:
        print(f"\nA poção evapora... o número era {numero_secreto}! 🕸️")

if __name__ == "__main__":
    adivinha_doces()
