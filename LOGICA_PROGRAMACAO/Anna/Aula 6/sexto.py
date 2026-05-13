#1 
# modelo = input("Qual o modelo do seu veiculo?")
# placa = input("Qual a placa do seu veiculo?")
# print(f"Veículo {modelo} de placa {placa} registrado no sistema. Boa viagem!")

#2
# print("Cálculo de Autonomia")
# tanque = float(input("Qual é a capacidade de seu tanque em Litros?"))
# consumo = float(input("Digite o consumo médio por caminhão em Km/L"))
# total = tanque / consumo 
# print(f"Seu caminhão pode percorrer {total:.2f} em Km/l")
# print("Seu caminhão pode percorrer", round(total,20), "em Km/l")

#3
# print("Conversor de Moeda (Frete Internacional)")
# valor_reais = float(input("Qual é o valor em Reais que será convertido?..."))
# taxa_dolar = float(input("Qual é o valor da taxa em dolar em Reais?..."))
# total = valor_reais / taxa_dolar 
# print(f"O valor total convertido é... {total:.2f}")

#4
# print("Média de Entrega")
# tempo1 = int(input("Qual foi o tempo para concluir a rota 1 em horas"))
# tempo2 = int(input("Qual foi o tempo para concluir a rota 2 em horas"))
# tempo3 = int(input("Qual foi o tempo para concluir a rota 3 em horas"))
# media = (tempo1 + tempo2 + tempo3) / 3
# print(f"A média {media:.2f} de tempo das entregas")

#5
# print("Monitor de Carga")
# peso = float(input("Qual é o peso atual do seu caminhão?..."))

# if peso < 10:
#     print("Carga Leve")
# elif peso <= 25:
#     print("carga padrão")
# else:
#     print("ALERTA: Excesso de Peso!")

#6
# print("Classificador de Destinos ")
# print("Regiões = N - Região Norte , S - Região Sul , qualquer outra - internacional")
# regiao = input("Inserir o código da região: ").lower()
# if regiao == "N".upper() or regiao == "n".lower():
#     print("Região Norte")
# elif regiao == "S":
#     print("Região Sul")
# else:
#     print("região internacional")

#7 
# print("Liberação de saída")
# checklist = input("o checklist foi concluído? [concluído ou Não Concluído ]")
# motorista = input("O motorista foi identificado? [sim ou não]")
# if checklist == "concluído" and motorista == "Sim":
#     print("Veículo autorizado a iniciar a rota.")
# else: 
#     print("Veículo NÂO autorizado a iniciar a rota. Verificar checklist e identificação do motorista.")

#8
# print("Calculo de atrasos")
# total_entregas = int(input("Total de Entregas Agendadas..."))
# total_atrasos = int(input("Total de Entregas em Atrasos..."))
# if total_atrasos > total_entregas * 0.1:
#     print("Necessario otimizar rotas")
# else:
#     print("Logística Eficiente")

 #9
# print("Validação de Calibragem")
# pressao = float(input("Digite a pressão do pneu em PSI:..."))
# if 100 <= pressao <= 110:
#     print("Dentro do padrão")
# elif pressao < 100:
#     print("Abaixo do recomendado")
# else:
#     print("Acima do recomendado")

 #10
# print("Contagem de Embarque")
# import time 
# for contagem in range(5,0,-1):
#     time.sleep(1)
#     print(contagem)
# print("Portão Trancado")

#11
# print("Somatório de Frete (Acumulador)")
# total =  0 
# while True: 
#    valor = float(input("Valor do Frete: "))
#    if valor == 0:
#     total += valor  
#    print(f"Total acumulado {total} do frete")

 #11.2
# print("Somatório de Frete (Acumulador)")
# faturamento_total = 0 
# valor_frete = -1
# while valor_frete !=0:
#     valor_frete = float(input("Valor do Frete ou 0 para encerrar"))
#     faturamento_total += valor_frete
#     print(f"Faturamento acumulado: R$ {faturamento_total}")  
# print("Cálculo executado com sucesso") 

# 11.3
# print("somatório de Frete (Acumulador)")
# b = 0 
# while True:
#     t = int(input("Valor Frete..."))
#     c = input("Quer continuar s/n")
#     b += t 
#     if c == "s":
#         continue 
#     else: 
#         break 
# print(f"Faturamento total{b}acumulado")

#12
# print("Monitoramento de Frota")
# maior_km = 0
# for frota in range(1, 6):
#     km = float(input(f"Digite a quilometragem de veículo {frota}:"))
#     if km > maior_km:
#         maior_km = km 
#     print(f"A maior quilometragem registrada é: {maior_km} km.")

#13
# print("Sistema de Rastreio")
# codigo_correto = "track99"
# tentativas = 0 
# max_tentativas = 3 
# while tentativas < max_tentativas:
#     codigo_input = input("Código de acesso para o ratreador: :)")
#     if codigo_input == codigo_correto:
#         print("Acesso permitido. Iniciando rastreamento...")
#         break 
#     else:
#         tentativas += 1 
#         print("Acesso negado")
#         if tentativas < max_tentativas: 
#             print(f"Tentativas restantes {max_tentativas-tentativas}")
#         else: 
#             print("Rastreamento Bloqueado")