import customtkinter as ctk
from usuarios_json import cadastrar_usuario

def criar_pagina_cadastro(container, mostrar_mensagem, voltar):
    frame = ctk.CTkFrame(container)
    frame.grid(row=0, column=0, sticky="nsew")

    label_titulo = ctk.CTkLabel(frame, text='Cadastro de Novo Usuário', font=("Arial", 22))
    label_titulo.pack(pady=20)

    campo_nome = ctk.CTkEntry(frame, placeholder_text='Nome completo', width=300)
    campo_nome.pack(pady=10)

    campo_usuario = ctk.CTkEntry(frame, placeholder_text='Novo usuário', width=300)
    campo_usuario.pack(pady=10)

    campo_senha = ctk.CTkEntry(frame, placeholder_text='Nova senha', show='*', width=300)
    campo_senha.pack(pady=10)

    def cadastrar():
        nome = campo_nome.get()
        usuario = campo_usuario.get()
        senha = campo_senha.get()

        if nome and usuario and senha:
            if cadastrar_usuario(nome, usuario, senha):
                mostrar_mensagem("Usuário cadastrado com sucesso!", "green")
                voltar()
            else:
                mostrar_mensagem("Erro: nome de usuário já existe.", "red")
        else:
            mostrar_mensagem("Preencha todos os campos.", "red")

    ctk.CTkButton(frame, text='Cadastrar', command=cadastrar, width=200, fg_color='red').pack(pady=10)
    ctk.CTkButton(frame, text='Voltar', command=voltar, width=200, fg_color='red').pack(pady=20)

    return frame
