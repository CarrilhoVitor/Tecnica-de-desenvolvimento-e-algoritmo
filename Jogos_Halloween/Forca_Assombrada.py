import random
import time
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def linha():
    print("🕸️" * 40)

def print_lento(texto, atraso=0.03):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(atraso)
    print()

def forca_assombrada():
        limpar_tela()
        linha()
        print("🎃  FORCA ASSOMBRADA  🎃")
        linha()
        print("\nAdivinhe a palavra antes que o monstro te encontre...\n")

        palavras = {
            "fantasma": "Assombra castelos antigos...",
            "bruxa": "Adora voar em noites de lua cheia.",
            "abobora": "Símbolo clássico do Halloween.",
            "zumbi": "Voltou dos mortos e anda bem devagar.",
            "aranha": "Costuma morar nos cantos escuros.",
            "caveira": "Representa a morte... e o mistério."
        }

        palavra, dica = random.choice(list(palavras.items()))
        letras_descobertas = ["_" for _ in palavra]
        tentativas = 6
        usadas = set()

        print(f"Dica: {dica}\n")

        def mostrar_forca(erros):
            estagios = [
                "   -----\n   |   |\n   |   O\n   |  /|\\\n   |  / \\\n  _|_",
                "   -----\n   |   |\n   |   O\n   |  /|\\\n   |  /\n  _|_",
                "   -----\n   |   |\n   |   O\n   |  /|\\\n   |\n  _|_",
                "   -----\n   |   |\n   |   O\n   |  /|\n   |\n  _|_",
                "   -----\n   |   |\n   |   O\n   |   |\n   |\n  _|_",
                "   -----\n   |   |\n   |   O\n   |\n   |\n  _|_",
                "   -----\n   |   |\n   |\n   |\n   |\n  _|_"
            ]
            print(estagios[6 - erros])

        while tentativas > 0 and "_" in letras_descobertas:
            print("Palavra:", " ".join(letras_descobertas))
            print("Letras usadas:", " ".join(sorted(usadas)) or "(nenhuma)")
            mostrar_forca(tentativas)
            palpite = input("\nDigite uma letra: ").lower().strip()

            if not palpite.isalpha() or len(palpite) != 1:
                print("Digite apenas uma letra válida!")
                continue
            if palpite in usadas:
                print("Você já tentou essa letra.")
                continue

            usadas.add(palpite)
            limpar_tela()
            if palpite in palavra:
                for i, c in enumerate(palavra):
                    if c == palpite:
                        letras_descobertas[i] = palpite
                print("🎃 Boa! Você acertou uma letra!")
            else:
                tentativas -= 1
                print("👻 Letra errada! O monstro está chegando...")
            print()
            time.sleep(1)

        if "_" not in letras_descobertas:
            print(f"\n✨ Você escapou! A palavra era **{palavra.upper()}**! ✨")
        else:
            mostrar_forca(0)
            print(f"\n💀 Você perdeu! A palavra era **{palavra.upper()}**...")

if __name__ == "__main__":
    forca_assombrada()
