#Funções são blocos de código reutilizáveis
#O "f" no python, usado antes das aspas de uma string (como f"texto{variável}"), indica que se trata de uma f-string (ou formatted string literal). Ele informa ao python que a string contém expressões entre chaves {} que devem ser avaliadas em tempo de execução e substituídas pelos seus valores reais. 

# def saudacao(nome):
#    return f"Olá,{nome}!"

# mensagem = saudacao("Anna")
# print(mensagem)

# def age(idade):
#    return f"sua idade é, {idade}!"
# mensagem = age ("16")
# print (mensagem)

def boas_vindas(nome, cargo):
   print(f"Olá, {nome}! Você é o novo {cargo}.")

   boas_vindas("Anna", "Personal Trainer")
   boas_vindas("Pulgar", "Ao Flamengo")
   boas_vindas("Matheus Cunha", "Novo goleiro do Flamengo")

   #Conversoes
nome = input("Seu nome: ")
idade= int(input("Sua idade: ")) #converte textos para inteiro 
print(f"{nome} tem {idade} anos.")

