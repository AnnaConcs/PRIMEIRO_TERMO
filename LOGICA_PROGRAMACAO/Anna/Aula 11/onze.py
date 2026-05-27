# Interface Gráfica com Tkinter 

# Os componentes principais (Widgets)
# Tk: Janela principal
# Label: É o texto a digitar 
# Button: Botão clicável de evento 
# Entry: caixa de texto = input 

# 0. Biblioteca
import tkinter as tk
from tkinter import messagebox 

# 1. Criar janela
janela = tk.Tk()
janela.title("Minha Primeira Janela em GUI")
janela.geometry("1000x400")

# 2. Criar função do botão 
def mostrar_mensagem():
    messagebox.showinfo("Sucesso", "Você clicou no botão :)")

# 3. Criar os componentes
lbl_titulo_pagina = tk.Label(janela, text = "Bem-vindo a aula de interface Gráfica em Python", font = ("Arial", 14, "bold"))
lbl_mensagem_linha2_pagina = tk.Label(janela, text = "Flamengo melhor time!! O resto é cópia mal feita", font = ("Arial", 12, "bold"))
btn_clique_ativar = tk.Button(janela, text = "Clique Aqui :)", font=("Arial", 14), bg="#c00c0c", fg="White", command = mostrar_mensagem)
btn_clicar_fechar = tk.Button(janela, text ="Fechar Aplicativo", command = janela.destroy)
lbl_titulo_pagina.grid(row=3, column=5, padx=10, pady=10)
btn_clique_ativar.grid(row=3, column=1, padx=15, pady=15)
btn_clicar_fechar.grid(row=3, column=4, padx=15, pady=15)
lbl_mensagem_linha2_pagina.grid(row=3, column=1, padx=10, pady=10)
# 4. Posicionar os componentes na janela
# lbl_titulo_pagina.pack(pady=5) #adiciona espaçamento
# btn_clique_ativar.pack(pady=10)
# btn_clicar_fechar.pack(pady=15)



# 5. Rodar Interface
janela.mainloop()