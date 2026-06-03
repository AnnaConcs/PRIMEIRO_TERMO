# Biblioteca
import tkinter as tk
from tkinter import messagebox, ttk
# Criar 
biblioteca = tk.Tk()
biblioteca.title("biblioteca")
biblioteca.geometry("500x500")

# 2. Criar função do botão 
def mostrar_mensagem():
    messagebox.showinfo("Você fez o empréstimo", "ótima leitura :)")

# 3. Criar os componentes
lbl_mensagem_usuario = tk.Label(biblioteca, text="Digite seu nome :)")
lbl_mensagem_usuario.grid(row=0, column=0, pady=10, padx=10)
lbl_mensagem_livro = tk.Label(biblioteca, text="Digite o nome do seu livro :)")
lbl_mensagem_livro.grid(row=1, column=0, pady=10, padx=10)

lbl_mensagem_usuario = tk.Label(biblioteca, text="Tipo de usuário:")
lbl_mensagem_usuario.grid(row=2, column=0, pady=10, padx=10)

lbl_mensagem_usuario = tk.Label(biblioteca, text="Categoria do Livro:")
lbl_mensagem_usuario.grid(row=3, column=0, pady=10, padx=10)

lbl_mensagem_usuario = tk.Label(biblioteca, text="Dias de Empréstimo:")
lbl_mensagem_usuario.grid(row=4, column=0, pady=10, padx=10)

# Entrys
usuario_nome = tk.Entry(biblioteca, font=("Arial", 12), width=20)
usuario_nome.grid(row=0,column=1,pady=10,padx=10)

tipo_de_usuario = tk.Entry(biblioteca, font=("Arial", 12), width=20 )
tipo_de_usuario.grid(row=1,column=1,pady=10,padx=10)



# Componentes de ComboBox
combo_nivel = tk.ttk.Combobox(biblioteca, values=["[1] Aluno", "[2] Comunidade Geral"], width=30)
combo_nivel.grid(row=2, column=1, pady=10, padx=10)

combo_nivel = tk.ttk.Combobox(biblioteca, values=["Normal", "Raro"], width=30)
combo_nivel.grid(row=3, column=1, pady=10, padx=10)

combo_nivel = tk.ttk.Combobox(biblioteca, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], width=30)
combo_nivel.grid(row=4, column=1, pady=10, padx=10)

# Fechar biblioteca e validar empréstimo
btn_validar_emprestimo = tk.Button(biblioteca, text="Validar Empréstimo", command=mostrar_mensagem, bg="#c00c0c", fg="White")
btn_validar_emprestimo.grid(row=6, column=0, pady=10, padx=10)

btn_fechar_janela = tk.Button(biblioteca, text="Fechar janela", command=biblioteca.destroy, bg="#c00c0c", fg="White")
btn_fechar_janela.grid(row=7, column=0, pady=10, padx=10)


# 5. Rodar Interface
biblioteca.mainloop()