# Foco: print, input, operações matemáticas e f-strings
# 1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"
# import tkinter as tk
# from tkinter import messagebox, ttk

# def registro():
#     # .get() serve para buscar o texto da caixa
#     nome_operador = operador_nome.get()
#     turno_operador = combo_nivel.get()
    
#     if nome_operador == "" and turno_operador == "":
#         messagebox.showwarning("Aviso", "Digite Seu Nome e seu Turno!")

#     else:
#         messagebox.showinfo("Bem-Vindo!", f"Operador {nome_operador}, registrado no Turno {turno_operador}. Boa jornada ")

# janela_registro = tk.Tk()
# janela_registro.title("Registro do Operador")
# janela_registro.geometry("500x500")


# lbl_mensagem_operador = tk.Label(janela_registro, text="Digite seu nome :)")
# lbl_mensagem_operador.grid(row=0, column=0, pady=10, padx=10)
# lbl_mensagem_turno = tk.Label(janela_registro, text="Qual seu Turno?")
# lbl_mensagem_turno.grid(row=1, column=0, pady=10, padx=0)

# combo_nivel = tk.ttk.Combobox(janela_registro, values=["A","B","C"], width=30)
# combo_nivel.grid(row=1, column=1, pady=10, padx=10)

# operador_nome = tk.Entry(janela_registro, font=("Arial", 12), width=20)
# operador_nome.grid(row=0,column=1,pady=10,padx=10)

# # operador_turno = tk.Entry(janela_registro, font=("Arial", 12), width=20 )
# # operador_turno.grid(row=1,column=1,pady=10,padx=10)

# # Botão
# btn_enviar_mensagem = tk.Button(janela_registro, text="Registrar Turno", command=registro,bg="#c00c0c", fg="White")
# btn_enviar_mensagem.grid(row=4, column=0, pady=10, padx=10)

# btn_fechar_janela = tk.Button(janela_registro, text="Fechar janela", command=janela_registro.destroy, bg="#c00c0c", fg="White")
# btn_fechar_janela.grid(row=7, column=0, pady=10, padx=10)


# janela_registro.mainloop()

# 2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.
# import tkinter as tk
# from tkinter import messagebox
# #def
# def producao():
#     calculo_peca = int(peca_calculo.get())

#     if calculo_peca == "" :
#         messagebox.showwarning("Aviso", "Preencha o campo em branco!" )
#     else:
#         total = calculo_peca * 8
#         messagebox.showinfo("Bem-Vindo",f"O total de peças produzidas em um turno de 8h será de {total} peças.")
# #janela
# janela_producao = tk.Tk()
# janela_producao.title("Produção de Peças")
# janela_producao.geometry("500x500")
# #componentes, Labels
# lbl_mensagem_producao = tk.Label(janela_producao, text="Digite o número de peças produzidas em 1h")
# lbl_mensagem_producao.grid(row=0, column=0, pady=10, padx=10)
# # Entrys
# peca_calculo = tk.Entry(janela_producao, font=("Arial", 12), width=20)
# peca_calculo.grid(row=0,column=1,pady=10,padx=10)
# # Botão
# btn_enviar_mensagem = tk.Button(janela_producao, text="Calcular", command=producao,bg="#c00c0c", fg="White")
# btn_enviar_mensagem.grid(row=4, column=0, pady=10, padx=10)
# btn_fechar_janela = tk.Button(janela_producao, text="Fechar Janela", command=janela_producao.destroy, bg="#c00c0c", fg="White")
# btn_fechar_janela.grid(row=7, column=0, pady=10, padx=10)
# janela_producao.mainloop()
# 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# ≈ 14.5 PSI) e exiba com duas casas decimais.
# import tkinter as tk
# from tkinter import messagebox
# def conversor():
#     calculo_conversor = float(conversor_calculo.get())

#     if calculo_conversor == "" :
#         messagebox.showwarning("Aviso", "Preencha o campo em branco!")
#     else:
#         total = calculo_conversor * 14.5
#         messagebox.showinfo("Bem-Vindo",f"A conversão em PSI é um total de {total}!")
# #janela
# janela_conversor = tk.Tk()
# janela_conversor.title("Conversor de Unidade")
# janela_conversor.geometry("500x500")
# #componentes, Labels
# lbl_mensagem_conversor = tk.Label(janela_conversor, text="Digite o número que quer converter para PSI")
# lbl_mensagem_conversor.grid(row=0, column=0, pady=10, padx=10)
# # Entrys
# conversor_calculo = tk.Entry(janela_conversor, font=("Arial", 12), width=20)
# conversor_calculo.grid(row=0,column=1,pady=10,padx=10)
# # Botão
# btn_enviar_mensagem = tk.Button(janela_conversor, text="Converter", command=conversor,bg="#c00c0c", fg="White")
# btn_enviar_mensagem.grid(row=4, column=0, pady=10, padx=10)
# btn_fechar_janela = tk.Button(janela_conversor, text="Fechar Janela", command=janela_conversor.destroy, bg="#c00c0c", fg="White")
# btn_fechar_janela.grid(row=7, column=0, pady=10, padx=10)
# janela_conversor.mainloop()
# 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.
# 5. Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".
# import tkinter as tk
# from tkinter import messagebox
# def Termostato():
#     Termostato_Temperatura = int(Temperatura_Termostato.get())
#     if Termostato_Temperatura <= 40:
#         messagebox.showinfo("Aviso",f"Baixa Carga")
#     elif Termostato_Temperatura >= 70:
#         messagebox.showinfo("ALERTA!!!", "Resfriamento Ativado")
#     else:
#         messagebox.showinfo("Aviso", "Normal")
# #janela
# janela_Termostato = tk.Tk()
# janela_Termostato.title("Termostato Inteligente")
# janela_Termostato.geometry("500x500")
# #componentes, Labels
# lbl_mensagem_conversor = tk.Label(janela_Termostato, text="Digite a Temperatura do motor")
# lbl_mensagem_conversor.grid(row=0, column=0, pady=10, padx=10)
# # Entrys
# Temperatura_Termostato = tk.Entry(janela_Termostato, font=("Arial", 12), width=20)
# Temperatura_Termostato.grid(row=0,column=1,pady=10,padx=10)
# # Botão
# btn_enviar_mensagem = tk.Button(janela_Termostato, text="Temperatura do Motor", command=Termostato,bg="#c00c0c", fg="White")
# btn_enviar_mensagem.grid(row=4, column=0, pady=10, padx=10)
# btn_fechar_janela = tk.Button(janela_Termostato, text="Fechar Janela", command=janela_Termostato.destroy, bg="#c00c0c", fg="White")
# btn_fechar_janela.grid(row=7, column=0, pady=10, padx=10)
# janela_Termostato.mainloop()
# 6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".
# import tkinter as tk
# from tkinter import messagebox, ttk
# def Classificador():
#     Classificador_Lotes = Lotes_Classificador.get()
#     if Classificador_Lotes  == "A":
#         messagebox.showwarning("Aviso", "Você escolheu Alimentos")
#     elif Classificador_Lotes == "E":
#          messagebox.showwarning("Aviso", "Você escolheu Eletrônicos")
#     else:
#         messagebox.showinfo("Aviso", "Lote Desconhecido")
# #janela
# janela_Lotes = tk.Tk()
# janela_Lotes.title("Classificador de Lotes")
# janela_Lotes.geometry("500x500")
# #componentes/Labels
# lbl_mensagem_Lotes = tk.Label(janela_Lotes, text="Digite a letra A, para Alimentos. E, Eletrônicos. Qualquer outra, Desconhecido")
# lbl_mensagem_Lotes.grid(row=0, column=0, pady=10, padx=10)
# #Entrys
# Lotes_Classificador = tk.Entry(janela_Lotes, font=("Arial", 12), width=20)
# Lotes_Classificador.grid(row=1,column=0,pady=10,padx=10)
# # Botão
# btn_enviar_mensagem = tk.Button(janela_Lotes, text="Classificar Lote", command=Classificador,bg="#c00c0c", fg="White")
# btn_enviar_mensagem.grid(row=4, column=0, pady=10, padx=10)
# btn_fechar_janela = tk.Button(janela_Lotes, text="Fechar janela", command=janela_Lotes.destroy, bg="#c00c0c", fg="White")
# btn_fechar_janela.grid(row=7, column=0, pady=10, padx=10)
# # Rodar interface
# janela_Lotes.mainloop()
#7.Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
#botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
#iniciar.
# import tkinter as tk
# from tkinter import messagebox, ttk
# def Seguranca():
#     sensor_porta = combo_nivel_sensor.get()
#     botao_emergencia = combo_nivel_emergencia.get()
#     if sensor_porta  == "Fechado" and botao_emergencia == "Desligado":
#         messagebox.showwarning("Aviso", "Porta Fechada e Botão desligado. Pode iniciar")
#     else:
#          messagebox.showinfo("Aviso", "Porta aberta, Botão ligado. não pode iniciar")
# #janela
# janela_Seguranca = tk.Tk()
# janela_Seguranca.title("Segurança de Operação")
# janela_Seguranca.geometry("500x500")
# #componentes/Labels
# lbl_mensagem_Lotes = tk.Label(janela_Seguranca, text="Selecione as informações corretas para saber se pode iniciar ou não")
# lbl_mensagem_Lotes.grid(row=0, column=0, pady=10, padx=10)
# #Entrys
# # botao_emergencia = tk.Entry(janela_Seguranca, font=("Arial", 12), width=20)
# # botao_emergencia.grid(row=1,column=0,pady=10,padx=10)
# #Componentes de ComboBox
# combo_nivel_sensor = tk.ttk.Combobox(janela_Seguranca, values=["Ligado", "Fechado", "Desligado", "Aberto"], width=30)
# combo_nivel_sensor.grid(row=2, column=0, pady=10, padx=10)
# combo_nivel_emergencia = tk.ttk.Combobox(janela_Seguranca, values=["Ligado", "Fechado", "Desligado", "Aberto"], width=30)
# combo_nivel_emergencia.grid(row=3, column=0, pady=10, padx=10)
# #Botão
# btn_enviar_mensagem = tk.Button(janela_Seguranca, text="Confirmar", command=Seguranca,bg="#c00c0c", fg="White")
# btn_enviar_mensagem.grid(row=4, column=0, pady=10, padx=10)
# btn_fechar_janela = tk.Button(janela_Seguranca, text="Fechar janela", command=janela_Seguranca.destroy, bg="#c00c0c", fg="White")
# btn_fechar_janela.grid(row=7, column=0, pady=10, padx=10)
# #Rodar interface
# janela_Seguranca.mainloop()
# 8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
# o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
# "Processo Otimizado".
# import tkinter as tk
# from tkinter import messagebox
# def Calculo():
#     pecas_produzidas = int(ent_pecas_defeituosas.get())
#     total_defeituosas = int(ent_total_defeituosas.get())
    
#     if pecas_produzidas  > total_defeituosas:
         
#          messagebox.showwarning("Aviso", "O Processo de descarte foi Otimizado")
#     elif total_defeituosas > 5:
#           total_porc = total_defeituosas - pecas_produzidas * 0.05
#           messagebox.showinfo("Aviso", f"Revisar Processo {total_porc}")
# #janela
# janela_calculo = tk.Tk()
# janela_calculo.title("Processo Otimizado")
# janela_calculo.geometry("500x500")
# #componentes/Labels
# lbl_mensagem_Lotes = tk.Label(janela_calculo, text="Qual o total de peças produzidas?")
# lbl_mensagem_Lotes.grid(row=0, column=0, pady=10, padx=10)
# lbl_total_descarte = tk.Label(janela_calculo, text="Qual o total de peças produzidas?")
# lbl_total_descarte.grid(row=1, column=0, pady=10, padx=10)

# #Entrys
# ent_pecas_defeituosas = tk.Entry(janela_calculo, font=("Arial", 12), width=20)
# ent_pecas_defeituosas.grid(row=0,column=1,pady=10,padx=10)
# ent_total_defeituosas = tk.Entry(janela_calculo, font=("Arial", 12), width=20)
# ent_total_defeituosas.grid(row=1,column=1,pady=10,padx=10)


# #Botão
# btn_enviar_mensagem = tk.Button(janela_calculo, text="Fazer Cálculo", command=Calculo,bg="#c00c0c", fg="White")
# btn_enviar_mensagem.grid(row=4, column=0, pady=10, padx=10)
# btn_fechar_janela = tk.Button(janela_calculo, text="Fechar janela", command=janela_calculo.destroy, bg="#c00c0c", fg="White")
# btn_fechar_janela.grid(row=7, column=0, pady=10, padx=10)
# #Rodar interface
# janela_calculo.mainloop()
# 9. Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
# diga se está dentro da tolerância, acima ou abaixo.
# import tkinter as tk
# from tkinter import messagebox
# def Validacao():
#     pecas_medida = float(medida_pecas.get())
#     if pecas_medida  > 9.8 and pecas_medida < 10.2:
#         messagebox.showwarning("Aviso", "Abaixo da Tolerância")
#     elif pecas_medida > 10.2:
#         messagebox.showwarning("Aviso", "Acima da Tolerância")
#     else:
#         messagebox.showwarning("Aviso", "Dentro da Tolerância")
# #janela
# janela_Validacao = tk.Tk()
# janela_Validacao.title("Validação de Medida")
# janela_Validacao.geometry("500x500")
# #componentes/Labels
# lbl_mensagem_Lotes = tk.Label(janela_Validacao, text="Qual a medida da peça?")
# lbl_mensagem_Lotes.grid(row=0, column=0, pady=10, padx=10)
# #Entrys
# medida_pecas = tk.Entry(janela_Validacao, font=("Arial", 12), width=20)
# medida_pecas.grid(row=0,column=1,pady=10,padx=10)
# #Botão
# btn_enviar_mensagem = tk.Button(janela_Validacao, text="Conferir Medida", command=Validacao,bg="#c00c0c", fg="White")
# btn_enviar_mensagem.grid(row=4, column=0, pady=10, padx=10)
# btn_fechar_janela = tk.Button(janela_Validacao, text="Fechar janela", command=janela_Validacao.destroy, bg="#c00c0c", fg="White")
# btn_fechar_janela.grid(row=7, column=0, pady=10, padx=10)
# #Rodar interface
# janela_Validacao.mainloop()
# 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.
import tkinter as tk
from tkinter import messagebox
def Qualidade():
    media_qualidade = int(qualidade_media.get())
    if media_qualidade == 