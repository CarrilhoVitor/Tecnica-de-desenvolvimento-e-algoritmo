produtos_cadastrados = {}

print("Cadastro de Produtos")
print("--------------------")

nome_p1 = input("Digite o nome do primeiro produto: ")
preco_p1_str = input(f"Digite o PREÇO de '{nome_p1}': R$ ").replace(',', '.')

try:
    preco_p1 = float(preco_p1_str)
    produtos_cadastrados[nome_p1] = preco_p1
except ValueError:
    print("❌ Preço inválido para o produto 1. Usando 0.00.")
    produtos_cadastrados[nome_p1] = 0.00

nome_p2 = input("\nDigite o nome do segundo produto: ")
preco_p2_str = input(f"Digite o PREÇO de '{nome_p2}': R$ ").replace(',', '.')

try:
    preco_p2 = float(preco_p2_str)
    produtos_cadastrados[nome_p2] = preco_p2
except ValueError:
    print("❌ Preço inválido para o produto 2. Usando 0.00.")
    produtos_cadastrados[nome_p2] = 0.00

print("\n Cadastro Finalizado.")
print("--- Dicionário de Produtos ---")

print(produtos_cadastrados)
