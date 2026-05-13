# Clean Code - Aula 7
# Para que usar? 
# Como usar?

# print("Clean Code - Aula 7")
# aula = 7
# print(f"Estamos na aula {aula} de Clean Code")

# # Manipulação de Arquivos e texto
# manipular_texto = " Python ´é Muito Legal! "
# print(manipular_texto.strip().upper()) #PYTHON
# print(manipular_texto.strip().lower()) #"python"
# print(manipular_texto.strip().startswith("A")) # "Começar com letra Inicial"
# print(manipular_texto.strip().capitalize()) # "Letras Inicial"
# print(manipular_texto.strip().title()) # "Titulo"
# print(manipular_texto.strip().replace(" ", "_")) # "Prencher vazios"
# print(manipular_texto.strip().split()) # "Separar palavras"

# # Execício 1:
# # Crie um programa que peça ao usúario para inserir uma frase e, em seguida, exiba a frase com as seguintes transformações:
# # - Deixe o texto em letras minúsculas.
# frase_usuario = input("Digite uma frase:")
# print(frase_usuario.strip().lower())
 
# Manipular arquivos:
# Escrevendo
# with open("notas.txt", "w", encoding="utf-8") as texto:
#     texto.write("Estudar Python hoje!")
#     texto.write("\nLer sobre Clean Code.")
#     texto.write("\n Estamos evoluindo")
#     texto.write("\n quero ter uma R1")
# #Lendo
# with open ("notas.txt", "r", encoding="utf-8") as texto:
#     conteudo = texto.read()
# #     print(conteudo)
 
# Exemplo 1
# Crie um programa que leia o conteúdo de um arquivo de texto e conte quantas vezes a palavra "Python" aparece no arquivo. Exiba o resultado para o usuário
# with open ("notas.txt", "r", encoding="utf-8") as texto:
#     conteudo = texto.read()
#     contagem = conteudo.count("Python")
#     contagem = conteudo.upper().count("PYTHON") #Contar a palavra "Python"
#     contagem = conteudo.lower().count("python")
#     print(f"A contagem de palavras {contagem} é de...")

# Interação com o sistema operacional
import os # importa o módulo os para interagir com o sistema operacional

# Onde estou?
# print(os.getcwd())

# print(os.listdir())
# print(os.listdir("C:/Users"))

# Criar pastas
# os.mkdir("Anna")
# Criar arquivos

# Renomear pastas
# os.rename("Anna", "Minha_Pasta")

# Apagar pastas
os.rmdir("Minha_Pasta")
os.remove("notas.txt") #Excluir arquivos