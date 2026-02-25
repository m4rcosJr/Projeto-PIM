import customtkinter as ctk
from PIL import Image
import os
import sys
from pagina_login import criar_pagina_login
from pagina_de_cadastro import criar_pagina_cadastro
from pagina_principal import criar_pagina_principal
from questionario import criar_questionario
from curso import criar_curso
from seguranca_digital import criar_seg_digital
from questionario_seguranca import criar_questionario_seguranca


def recurso_caminho(rel_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, rel_path)

imagem_pil = Image.open(recurso_caminho("lgc1.png"))
imagem_login = ctk.CTkImage(dark_image=imagem_pil, size=(420, 420))

def main():
    ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    app.title("PIM")
    app.geometry("850x450")
    app.iconbitmap(recurso_caminho("imagem_2025-04-11_085255580.ico"))

    msg_label = ctk.CTkLabel(app, text="", font=("Arial", 16), text_color="green")
    def mostrar_mensagem(msg, cor="green"):
        msg_label.configure(text=msg, text_color=cor)
        msg_label.pack(pady=(5, 0))
        app.after(3000, lambda: msg_label.pack_forget())

    container = ctk.CTkFrame(app)
    container.pack(fill="both", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    # Declarar antes para usar nos lambdas
    pagina_login = None

    # Instanciações das páginas
    pagina_cadastro       = criar_pagina_cadastro(container, mostrar_mensagem, lambda: pagina_login.tkraise())
    seguranca_digital     = criar_seg_digital(container, lambda: pagina_principal.tkraise())
    quiz_seguranca        = criar_questionario_seguranca(container, lambda: pagina_principal.tkraise())
    pagina_principal      = criar_pagina_principal(
        container,
        lambda: pagina_login.tkraise(),
        lambda: mostrar_pagina(questionario),
        lambda: mostrar_pagina(curso),
        lambda: mostrar_pagina(seguranca_digital),
        lambda: mostrar_pagina(quiz_seguranca)
    )
    questionario          = criar_questionario(container, lambda: pagina_principal.tkraise())
    curso                 = criar_curso(container, lambda: pagina_principal.tkraise())
    pagina_login          = criar_pagina_login(container, lambda p: p.tkraise(), pagina_cadastro, pagina_principal, mostrar_mensagem, imagem_login)

    # Grid de todas as páginas
    for pagina in (
        pagina_login,
        pagina_cadastro,
        pagina_principal,
        questionario,
        curso,
        seguranca_digital,
        quiz_seguranca
    ):
        pagina.grid(row=0, column=0, sticky="nsew")

    pagina_login.tkraise()
    app.mainloop()

def mostrar_pagina(pagina):
    pagina.tkraise()

if __name__ == "__main__":
    main()
