# Registro de Veículo: Peça o modelo do veículo e a placa.
# ○ Exiba: "Veículo [Modelo] de placa [Placa] registrado no sistema. Boa
# viagem!"
# print("Bem-vindo")
# modelo = input("Qual o modelo do seu veiculo?")
# placa = input("Qual a placa do seu veiculo?")
# print(f"o modelo do seu carro é {modelo} e a placa do seu carro é {placa} eles foram registrados no sistema. Boa Viagem!")

# Cálculo de Autonomia: Peça a capacidade do tanque de combustível (em litros) e
# o consumo médio do caminhão (km/l).
# ○ Calcule e exiba a distância total que o veículo pode percorrer com o tanque
# cheio.
# print("olá")
# capacidade = float(input("Qual é a capacidade do seu tanque em Litros? "))
# consumo = float(input("Qual o consumo médio do seu caminhão km/l."))
# total = capacidade / consumo
# print("Seu veiculo vai percorrer", total)

# Conversor de Moeda (Frete Internacional): O sistema lê o valor de um frete em
# Dólar (USD).
# ○ Converta para Real (BRL) considerando a taxa de $1,00~USD \approx
# 5,00~BRL$ e exiba com duas casas decimais.
# print("Boa tarde")
# valor = float(input("Qual o valor em reais você quer converter? "))
# taxa = float(input("Qual é o valor do dólar em real?"))
# total = valor / taxa
# print("o valor total convertido é:", total)

# Média de Entrega: Peça o tempo de entrega (em horas) de 3 rotas diferentes
# realizadas por um motorista.
# ○ Exiba a média aritmética simples do tempo dessas entregas.
# print("olá")
# rota1 = int(input("Qual foi o tempo para concluir a entrega número 1 em horas?"))
# rota2 = int(input("Qual foi o tempo para concluir a rota número 2 em horas?"))
# rota3 = int(input("Qual foi o tempo para concluir a rota número 3 em horas?"))
# total = rota1 + rota2 + rota3 / 3
# print("O tempo total foi de:", total)

# 5 Monitor de Carga: Peça o peso atual de um caminhão em toneladas.
# ○ Abaixo de 10t: "Carga Leve".
# ○ Entre 10t e 25t: "Carga padrão".
# ○ Acima de 25t: "ALERTA: Excesso de Peso!".
# print("Bem-vindo")
# print("Verificar peso")
# peso = int(input("Digite o peso atual do caminhão: ")) 
# if peso <= 10:
#     print("Carga leve")
# elif peso <= 25:
#     print("Carga padrão")
# else:
#     print("ALERTA: Excesso de Peso!")

# 6. Classificador de Destino: O usuário insere o código da carga. Se começar com "N", exiba
# "Região Norte". Se começar com "S", "Região Sul". Para qualquer outro, "Região
# Internacional".
# print("Bem-vindo para onde vamos?")
# print("Classificador de destinos")
# print("Escolha uma das opções")
# print("Região Norte: N, Região Sul: S, para qualquer outra: Região Internacional")

# regiao = input("Digite uma opção: ")
# if regiao == "N":
#     print("Região Norte")
#     print("Obrigado e Boa viagem!")
# elif regiao == "S":
#     print("Região Sul")
#     print("Obrigado e Boa viagem!")
# else:
#     print("Região Internacional")
#     print("Obrigado e Boa viagem!")

#7 Liberação de Saída: O caminhão só pode sair se o checklist == "concluído" E o
# motorista_identificado == "sim".
# ○ Peça esses dois inputs e informe se o veículo está autorizado a iniciar a rota.
# print("Olá, Bem-vindo motorista")
# caminhao = input("qual o estado do checklist do caminhão?")
# check = input("O motorista foi identificado?")
# if caminhao == "concluido" and check == "sim":
#     print("Boa viagem!")

#8 Cálculo de Atrasos: Peça o total de entregas agendadas e o total de entregas realizadas
# com atraso.
# ○ Se o índice de atraso for maior que 10% do total, exiba "Necessário Otimizar
# Rotas", caso contrário, "Logística Eficiente".
# print("Olá, Boa tarde")
# agendadas = int(input("Qual seria o total de peças agendadas?"))
# atraso = int(input("Qual seria o total de peças realizadas com atrasado?"))
# entregastotais = agendadas + atraso
# porcentagem = entregastotais * 0.1
# if entregastotais >= porcentagem:
#     print("Necessario otimizar")
# else:
#     print("Logística insuficiente")

#9 Validação de Calibragem: Um pneu de carga deve ter pressão entre 100 PSI e 110 PSI.
#  Peça a medida e diga se está dentro do padrão, acima ou abaixo do recomendado.
# print("olá, Boa tarde")
# pneu = int(input("Qual seria a carga de pressão do seu pneu?"))
# if pneu == 100:
#     print("A carga de pressão está dentro do padrão")
# elif pneu >= 110:
#     print("A carga de pressão está acima do padrão")
# else:
#     print("A carga de pressão está abaixo do recomendado")

# 10.Contagem de Embarque: Use um for para fazer uma contagem regressiva de 5
# até 1 para o fechamento do portão de embarque e finalize com "Portão Trancado!".
print("olá, Boa tarde vamos iniciar a contagem regressiva")
for contagem in range(5,0,-1): 
    while contagem == 5:
     break
    print("5,4,3,2,1")
    continue