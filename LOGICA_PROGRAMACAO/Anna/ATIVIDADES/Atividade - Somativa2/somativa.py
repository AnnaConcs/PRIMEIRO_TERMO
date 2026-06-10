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
import tkinter as tk
from tkinter import messagebox
def Classificador():
    Classificador_Lotes = Lotes_Classificador.get
    if Classificador_Lotes  == "" :
        messagebox.showwarning("Aviso", "Preencha o campo em branco!")
    else:
        messagebox.showinfo("Bem-Vindo",f"")
