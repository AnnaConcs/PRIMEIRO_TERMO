#Exercício 1 
# Criar um algoritmo pergunte essas informações seu nome, idade, curso e seu hobbie e apresente no final o resultado 

print ("perguntas")
print ("iniciar perguntas")
pv1 = input("qual é o seu nome?: \n")
pv2 = int(input("qual é a sua idade?: \n"))
pv3 = input("qual curso voce está fazendo?: \n")
pv4= input("qual é o seu hobbie favorito?: \n")
print ("resultados", pv1,pv2,pv3,pv4)

#Exercício 2 
#Criar um algoritmo que pergunte o valor A e o valor B e apresente o resultado em um valor C

# print ("Cálculos")
# print ("iniciar cálculos")
# pv1 = int(input("Qual o valor de A?: \n"))
# pv2 = int(input("Qual o valor de B?: \n"))
# print("O Valor de C é:", pv1+pv2)

# #Exercício 3
# #Criar um algoritmo calcule sua viagem por 3 pedágios, em cada pedágio será cobrado um valor e no fim apresente o total das passagens 

# print ("Cálculos")
# print ("iniciar cálculos")
# pv1 = int(input("Qual o valor do pedágio 1?: \n"))
# pv2 = int(input("Qual o valor do pedágio 2?: \n"))
# pv3 = int(input("Qual o valor do pedágio 3?: \n"))
# print("O Valor total das passagens é:", pv1+pv2+pv3)

# #Exercício  4
# #Criar um algoritmo para calcular o IMC (indice de massa corporal). 
# #Para esse cálculo deverá ser peso / altura * altura ou peso / altura^2 ou por altura**

print ("Cálculos")
print ("iniciar cálculos")
mult1 = float(input("peso: \n"))
mult2 = float(input("altura: \n"))
print("O valor do IMC é:", mult1/(mult2*mult2))