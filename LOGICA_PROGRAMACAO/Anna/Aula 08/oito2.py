# Passo 1:  
# Perguntar informações sobre o veiculo ou forma de acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado 
# Se possuir erros informar ao usuario

print("Olá, seja Bem-vindo")
seu_veiculo = input("Qual seria seu veículo?: ")
placa_do_veiculo = input("Qual seria a placa do seu veiculo?: ")
print("Escolha uma opção de acesso Ticket ou TAG")
escolha = input("Digite uma opção: ")
if escolha == "Ticket":
    print("Você escolheu o Ticket, pressione o botão para retirar.")
    entrada_horario = input("Qual seria seu horário de entrada?")
    print(f"Ticket \n Veiculo/Modelo: {seu_veiculo} \n placa do veículo: {placa_do_veiculo} \n horário de entrada: {entrada_horario}")
elif escolha == "TAG":
    print("Você escolheu TAG")
    





