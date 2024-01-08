import tkinter as tk
from tkinter import PhotoImage
import string as st
import numpy as np

def gerar_senha():
    letras = st.ascii_letters
    numeros = st.digits
    especial = st.punctuation
    algarismo = letras + numeros + especial
    senha = np.random.choice(list(algarismo), 10)
    return ''.join(senha)

def on_button_click():
    nova_senha = gerar_senha()
    entry_senha.delete(0, tk.END)  # Limpa o conteúdo atual
    entry_senha.insert(0, nova_senha)  # Insere a nova senha na entrada

def copiar_senha():
    senha_para_copiar = entry_senha.get()
    janela.clipboard_clear()
    janela.clipboard_append(senha_para_copiar)
    janela.update()

# Criar a janela principal
janela = tk.Tk()
janela.title("Gerador de Senha Tkinter")

# Criar um campo de entrada
entry_senha = tk.Entry(janela, width=20, font=("Arial", 12), bd=5, relief=tk.GROOVE)
entry_senha.pack(pady=10)

# Carregar a imagem do ícone
copy_icon = PhotoImage(file="./images/copy_icon.png")

# Criar botões
botao_gerar = tk.Button(janela, text="Gerar Senha", command=on_button_click)
botao_gerar.pack(pady=5)

botao_copiar = tk.Button(janela, image=copy_icon, command=copiar_senha)
botao_copiar.pack(pady=5)

# Iniciar o loop principal da interface gráfica
janela.mainloop()
