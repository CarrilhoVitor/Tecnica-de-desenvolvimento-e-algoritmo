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

def aventura_fantasma():
    limpar_tela()
    linha()
    print("🏚️  A CASA DO FANTASMA 🕯️")
    linha()
    print()
    print_lento("Você e seus amigos entraram em uma velha mansão...")
    print_lento("As portas se fecharam sozinhas!")
    print_lento("Encontre a saída antes que o fantasma apareça...\n")

    escolha = input("Há três portas: esquerda, centro ou direita? ").lower()

    if escolha == "esquerda":
        print_lento("\nVocê entra em uma biblioteca antiga.")
        acao = input("Quer acender uma vela ou sair? (acender/sair): ")
        if acao == "acender":
            print_lento("A vela acende e revela uma passagem secreta! Você vence!")
        else:
            print_lento("Um espírito sai de um livro e te persegue! Fim!")

    elif escolha == "centro":
        print_lento("\nVocê sobe as escadas que rangem...")
        acao = input("Entrar no quarto iluminado ou no escuro? ")
        if acao == "iluminado":
            print_lento("Você encontra doces e um bilhete: 'Você está salvo!' 🍬")
        else:
            print_lento("Um espelho se quebra sozinho... algo sai dele! Fim!")

    elif escolha == "direita":
        print_lento("\nVocê entra na cozinha com um caldeirão borbulhante...")
        acao = input("Olhar dentro ou fugir? ")
        if acao == "olhar":
            print_lento("Um braço sai do caldeirão e te puxa! Fim!")
        else:
            print_lento("Você foge pelos fundos e escapa! 🎃")

    else:
        print_lento("Você hesita... o fantasma aparece! FIM!")

if __name__ == "__main__":
    aventura_fantasma()
