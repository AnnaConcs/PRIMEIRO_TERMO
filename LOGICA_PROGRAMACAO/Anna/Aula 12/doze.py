import tkinter as tk
from tkinter import messagebox, ttk

def bemvindo():
    # .get() serve para buscar o texto da caixa
    nome_usuario = usuario_nome.get()
    idade_usuario = usuario_idade.get()
    
    if nome_usuario == "" and idade_usuario == "":
        messagebox.showwarning("Aviso", "Por favor digite seu nome e idade! :)")

    else:
        messagebox.showinfo("Bem-Vindo", f"Olá {nome_usuario}, logando no sistema! e sua idade é {idade_usuario}")

def segunda_janela():
    segunda_janela = tk.Toplevel(janela_bemvindo)
    segunda_janela.title("Segunda Janela")
    segunda_janela.geometry("500x500")
    lbl_segunda_janela = tk.Label(segunda_janela, text="Bem-Vindo Flamenguista a sua segunda janela :), font=font=('Arial', 12), fg='blue'")
    lbl_segunda_janela.grid(row=0, column=0, pady=10, padx=10)
# Janela
janela_bemvindo = tk.Tk()
janela_bemvindo.title("Saudações do Usuário")
janela_bemvindo.geometry("500x500")

# Componentes
#Labels
lbl_mensagem_usuario = tk.Label(janela_bemvindo, text="Digite seu nome :)")
lbl_mensagem_usuario.grid(row=0, column=0, pady=10, padx=10)

lbl_mensagem_idade = tk.Label(janela_bemvindo, text="Digite sua idade :)")
lbl_mensagem_idade.grid(row=1, column=0, pady=10, padx=10)

lbl_mensagem_pais = tk.Label(janela_bemvindo, text="Escolha seu País :)")
lbl_mensagem_pais.grid(row=2, column=0, pady=10, padx=10)

# Entrys
usuario_nome = tk.Entry(janela_bemvindo, font=("Arial", 12), width=20)
usuario_nome.grid(row=0,column=1,pady=10,padx=10)

usuario_idade = tk.Entry(janela_bemvindo, font=("Arial", 12), width=20 )
usuario_idade.grid(row=1,column=1,pady=10,padx=10)

# Componentes de ComboBox
combo_nivel = tk.ttk.Combobox(janela_bemvindo, values=["Brasil", "Marrrocos", "Egito", "Escócia"], width=30)
combo_nivel.grid(row=2, column=1, pady=10, padx=10)

# Botão
btn_enviar_mensagem = tk.Button(janela_bemvindo, text="Enviar Mensagem", command=bemvindo,bg="#c00c0c", fg="White")
btn_enviar_mensagem.grid(row=4, column=0, pady=10, padx=10)

btn_segunda_janela = tk.Button(janela_bemvindo, text="abrir segunda janela",command=segunda_janela, bg="#c00c0c", fg="White")
btn_segunda_janela.grid(row=6, column=0, pady=30, padx=10)

btn_fechar_janela = tk.Button(janela_bemvindo, text="Fechar janela", command=janela_bemvindo.destroy, bg="#c00c0c", fg="White")
btn_fechar_janela.grid(row=7, column=0, pady=10, padx=10)

# Rodar interface
janela_bemvindo.mainloop()


