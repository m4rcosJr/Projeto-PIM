import customtkinter as ctk

def criar_pagina_principal(container, voltar,
                           ir_para_questionario,
                           ir_para_curso,
                           ir_para_seg_digital,
                           ir_para_quiz_seguranca):
    frame = ctk.CTkFrame(container, fg_color="transparent")
    frame.grid(row=0, column=0, sticky="nsew")
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # Cabeçalho
    header_frame = ctk.CTkFrame(frame, fg_color="transparent")
    header_frame.grid(row=0, column=0, sticky="ew", pady=(20, 10))
    header_frame.grid_columnconfigure(0, weight=1)
    ctk.CTkLabel(header_frame, text="PÁGINA INICIAL", font=("Arial", 22)).grid(row=0, column=0)

    # Menu
    content_frame = ctk.CTkFrame(frame, fg_color="transparent")
    content_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=20)
    content_frame.grid_columnconfigure(0, weight=1)
    content_frame.grid_columnconfigure(1, weight=0)
    content_frame.grid_columnconfigure(2, weight=1)
    content_frame.grid_rowconfigure(0, weight=1)

    menu_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
    menu_frame.grid(row=0, column=1, sticky="n")
    menu_frame.grid_columnconfigure(0, weight=1)
    menu_frame.grid_rowconfigure(4, weight=1)  # espaçador antes do "Sair"

    # Botões
    ctk.CTkButton(menu_frame, text="Questionário de Lógica",      width=250, fg_color="red", command=ir_para_questionario).grid(row=0, column=0, pady=(0,10))
    ctk.CTkButton(menu_frame, text="Curso de Lógica",             width=250, fg_color="red", command=ir_para_curso).grid(row=1, column=0, pady=(0,10))
    ctk.CTkButton(menu_frame, text="Curso de Segurança Digital",  width=250, fg_color="red", command=ir_para_seg_digital).grid(row=2, column=0, pady=(0,10))
    ctk.CTkButton(menu_frame, text="Questionário de Segurança",   width=250, fg_color="red", command=ir_para_quiz_seguranca).grid(row=3, column=0, pady=(0,10))
    ctk.CTkButton(menu_frame, text="Sair",                         width=250, fg_color="red", command=voltar).grid(row=5, column=0, pady=(40,0))

    return frame
