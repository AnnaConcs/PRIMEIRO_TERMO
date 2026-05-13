#Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado
# As entrada deverão ser registradas por placa.
#
# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado
# Se possuir erros informar ao usuário

# Passo 2:
# Verificar tempo de permanência
# Valor a ser cobrado

# Passo 3:
# Saída como será?
# Calcular tempo de permanência
# Se for TAG gerar na fatura da TAG
# Pagar ticket
# Devolver ticket na saída

# Passo 4:
# Gerar relatório de entradas e saídas
# Tratamento de Erros
# Revisão do código

#entrada
print("Olá, seja Bem-vindo")
entrada_horario = int(input("Qual seria seu horário de entrada?"))
print("Escolha uma opção de acesso Ticket ou TAG")
escolha = input("Digite uma opção: ")
if escolha == "Ticket":
    print("Você escolheu o Ticket, pressione o botão para retirar.")
    seu_veiculo = input("Qual seria o modelo do seu veículo?: ")
    placa_do_veiculo = input("Qual seria a placa do seu veiculo?: ")
    print(f"Ticket \n Veiculo/Modelo: {seu_veiculo} \n placa do veículo: {placa_do_veiculo} \n horário de entrada: {entrada_horario}")
elif escolha == "TAG":
    print("Carro identificado com TAG, Acesso Liberado!")
else:
    print("Erro de Acesso, pressione o interfone.")
     
 #saida
 
horario_saida = int(input("Qual seu horário de saída?"))
tempo_de_permanencia = entrada_horario - horario_saida
print(f"Seu tempo no local foi, {tempo_de_permanencia}")
total_estacionamento = tempo_de_permanencia * 12
print(f"O Valor a ser cobrado do estacionamento é de, {total_estacionamento} ")