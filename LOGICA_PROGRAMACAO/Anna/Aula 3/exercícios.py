# Exercícios 1 
# Criar um algoritmo para realizar a locação de filmes ou séries seguir o modelo anterior. Ao escolher a opção você deverá perguntar o nome do cliente do filme ou série e quantidade que deseja assim como o valor de aluguel
# Para filmes R$ 5,00 e para séries R$ 10,00

# print("Bem-Vindo ao nosso aluguel de filmes")
# print("Menu de Opção")
# print("Escolha uma das opções")
# print("Filmes F e Séries S e X para sair")

# escolha = input("Digite uma opção: ")

# if escolha == "F":
    print("Você está na sessão Filmes")
    nome = input("Digite seu nome")
    filme = input('Qual filme deseja?')
    quantidade = int(input("Qual quantidade deseja"))
    valor = 5 
    total = quantidade * valor
    print("Parabéns pela sua locação de filmes \n ", nome, "E seu filme foi: \n ", filme, "A quantidade foi \n ", quantidade, "O valor foi \n", valor, total )
# elif escolha == "S":
#     print("Você escolheu Séries")
#     print("Você está na sessão Séries")
#     nome = input("Digite seu nome")
#     série = input('Qual série deseja?')
#     quantidade = int(input("Qual quantidade deseja"))
#     valor = 10 
#     total = quantidade * valor
#     print("Parabéns pela sua locação de série \n ", nome, "E sua série foi: \n ", série, "A quantidade foi \n ", quantidade, "O valor foi \n", valor, total )
# else:
#     print("Você saiu do programa")

# Exercício 2 
# Loja de Comidas e Doces
# Criar um algoritmo para compra de produtos 
# 1 - Comida 
# 2 - Bebida 
# 3 - Doces 
# Ao escolher as opções cada um terá um valor de porcentagem, comida = 10%, bebida = 5%, Doces 2%
# Calcular  porcentagem valor / 100 ou valor * valor / 100 
 
# print("Bem-vindos a nossa loja de conveniências")
# print("Temos Comida, Bebida e Doce")
# print("Digite a opção que deseja para iniciar")
# print("Comida - Digite 1")
# print("Bebida - Digite 2")
# print("Doce - Digite 3")

# opcao= int(input("Digite sua opção"))
# if opcao == 1: 
#         print("Você está em Comida")
#         print("Temos PF,  À la carte")
#         comida = input("O que deseja?")
#         valor = float(input("Digite o valor da comida"))
#         desconto = valor * 10 / 100
#         total = valor - desconto 
#         print("Sua compra total foi de: ", total)
# elif opcao == 2:
#         print("Você está em Bebida")
#         print("Temos Coca, Àgua")
#         Bebida = (input("Digite o valor da Bebida"))
#         Bebida = input("O que deseja?")
#         valor = float(input("Digite o valor da bebida"))
#         desconto = valor * 10 / 100
#         total = valor - desconto 
#         print("Sua compra total foi de: ", total)
# elif opcao == 3: 
#         print("Você está em Doces")
#         print("Temos Chocolate, Brigadeiro")
#         Doce = (input("O que deseja?"))
#         valor = float(input("Digite o valor do Doce"))
#         desconto = valor * 10 / 100
        # total = valor - desconto 
        # print("Sua compra total foi de: ", total)
        # print("Obrigado por comprar conosco, bom apetite!!")    

# Exercício 3
# Calculadora com operadores 
# Sua calculadora deverá perguntar qual operador ele deseja e calcular os valores desejados. Operador = - / *

print ("Cálculos")
print ("iniciar cálculos")
print ("Qual conta você gostaria de fazer? A para Adição, S para Subtração, D para Divisão e M para Multiplicação")
escolha = input("Digite sua escolha")
if escolha == "A":
    A1 = int(input("Digite o primeiro valor : \n"))
    A2 = int(input("Digite o segundo valor : \n"))
    print("O valor da Adição ficou: \n" ,A1+A2)
elif escolha == "S":
    S1 = int(input("Digite o primeiro valor : \n"))
    S2 = int(input("Digite o segundo valor : \n"))
    print("O valor da Subtração ficou: \n" ,S1-S2)
elif escolha == "D":
    D1 = int(input("Digite o primeiro valor : \n"))
    D2 = int(input("Digite o segundo valor : \n"))
    print("O valor da Divisão ficou: \n" ,D1/D2)
elif escolha == "M":
    M1 = int(input("Digite o primeiro valor : \n"))
    M2 = int(input("Digite o segundo valor : \n"))
    print("O valor da Multiplicação ficou: \n" ,M1*M2)
else:
    print("Encerrrar calculadora")
   
#    Exercício 4
# Calculo de Notas 
# Nossas atividdes são por base de cálculo em somativa 1 e somativa 2, no final temos uma média. 
# Acima ou igual a 50 o aluno será aprovado caso contrario reprovado 
# o programa deverá perguntar o nome e as notas  apresentar o resultado final do aluno 


           


