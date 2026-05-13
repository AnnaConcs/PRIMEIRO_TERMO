# 1. O laço 'for' (Repetições Determinadas)
# Use o 'for' quando você sabe exatamente quantas vezes algo deve acontecer (como ler 10 sensores ou processar uma lista de peças).
# Exemplo: Relatório de Produção Diária 
# Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um: 

# Exemplo 1 
# for lote in range(1, 6):
#     print(f"Processando lote número {lote}...")
#     print("Qualidade verificada. [OK]")
#print("Produção do dia finalizada!")

# Exemplo 2 
# for b in range(10):
    # print(f"Quantidade total {b} foi...")

# Exemplo 3 
# Imagine o seguinte cenário, iremos produzir 20 discos de vinil
# for lote in range(1, 21):
#     print(f"Produzindo 20 discos de Vinil {lote}")
# print("20 discos de Vinil produzidos!")

# Exemplo 4
# pecas = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo", "Prego", "Chave de Fenda", "Alicate"]
# itempecas = ["Cilindrica", "Duplo", "Cônica", "Prego", "Orelha", "Redondo", "Phillips", "Universal"]

# for item in pecas:
#     print(f"Item em estoque: {item} e {itempecas}")


# Exemplo 5
# Imagine a seguinte situação gostaria de ter um menu onde pudesse perguntar qual opção você deseja e a partir da seleção ele listar os 
# produtos

# print("Bem-Vindo ao nosso restaurante!")
# print("Menu de comida")
# print("Escolha uma opção de comida")
# print("PF para pratos feitos, PD para pratos doces e B para bebidas")
# escolha = input("Digite uma opção: ")

# if escolha == "PF":
#     pratofeito = ["Arroz feijão, batata e bife", "macarronada", "lasanha"]
#     print("Você está na sessão de pratos feitos ")
#     # PF = input('Qual prato você deseja?')
#     for pf in pratofeito:
#         print(f"As opções de PF são {pf}")
#         escolha = input("Digite uma opção: ")

# if escolha == "PD":
#     pratodoce = ["Alfajor", "Gelatina", "Surpresa de uva"]
#     print("Você está na sessão de pratos doces ")
#     # PF = input('Qual prato você deseja?')
#     for pd in pratodoce:
#         print(f"As opções de PD são {pd}")
        
# elif escolha == "B":
#     bebida = ["Coca Cola", "água com gás", "Suco natural de laranja"]
#     print("Você está na sessão de bebidas")
#     # PF = input('Qual bebida você deseja?')
#     for B in bebida:
#         print(f"As opções de B são {B}")

# else:
#     print(f"Encerramos o sistema, obrigado pela preferência")
