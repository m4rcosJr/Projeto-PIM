import customtkinter as ctk
from usuarios_json import validar_login

def criar_pagina_login(container, mostrar_pagina, pagina_cadastro, pagina_principal, mostrar_mensagem,imagem_login):
    frame = ctk.CTkFrame(container)

    frame.grid(row=0, column=0, sticky="nsew")
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)

    frame_imagem = ctk.CTkFrame(frame, fg_color="transparent")
    frame_imagem.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    label_imagem = ctk.CTkLabel(frame_imagem, text="", image=imagem_login)
    label_imagem.pack(expand=True)

    frame_direita = ctk.CTkFrame(frame, fg_color="transparent")
    frame_direita.grid(row=0, column=1, sticky="nsew", padx=40, pady=40)

    label_usuario = ctk.CTkLabel(frame_direita, text='Usuário:', font=("Arial", 18))
    label_usuario.pack(pady=10)
    campo_usuario = ctk.CTkEntry(frame_direita, placeholder_text='Digite seu usuário', width=300)
    campo_usuario.pack(pady=10)

    label_senha = ctk.CTkLabel(frame_direita, text='Senha:', font=("Arial", 18))
    label_senha.pack(pady=10)
    campo_senha = ctk.CTkEntry(frame_direita, placeholder_text='Digite sua senha', show='*', width=300)
    campo_senha.pack(pady=10)

    def login():
        usuario = campo_usuario.get()
        senha = campo_senha.get()
        if validar_login(usuario, senha):
            mostrar_mensagem("Login bem-sucedido!", "green")
            mostrar_pagina(pagina_principal)
        else:
            mostrar_mensagem("Usuário ou senha inválidos.", "red")

    ctk.CTkButton(frame_direita, text='Login', command=login, width=200, fg_color='red').pack(pady=20)
    ctk.CTkButton(frame_direita, text='Cadastrar', command=lambda: mostrar_pagina(pagina_cadastro), fg_color='red', width=200).pack(pady=20)

    return frame
