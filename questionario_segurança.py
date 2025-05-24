# questionario_seguranca.py
import customtkinter as ctk
from functools import partial

def criar_questionario_seguranca(container, voltar):
    # Definição das perguntas e alternativas
    perguntas = [
        {
            "pergunta": "1. O que é phishing?",
            "alternativas": [
                "Uma senha segura",
                "Um tipo de vírus",
                "Uma tentativa de enganar usuários para roubar informações",
                "Um antivírus"
            ],
            "correta": 2
        },
        {
            "pergunta": "2. Qual destas senhas é mais segura?",
            "alternativas": [
                "123456",
                "senha123",
                "qwerty",
                "Y4*Tf@29q!mL"
            ],
            "correta": 3
        },
        {
            "pergunta": "3. O que é 2FA?",
            "alternativas": [
                "Um vírus de computador",
                "Um tipo de backup",
                "Um sistema de autenticação com duas etapas",
                "Um navegador seguro"
            ],
            "correta": 2
        },
        {
            "pergunta": "4. Qual a melhor prática ao usar Wi-Fi público?",
            "alternativas": [
                "Acessar banco normalmente",
                "Usar VPN",
                "Compartilhar arquivos pessoais",
                "Baixar programas aleatórios"
            ],
            "correta": 1
        },
        {
            "pergunta": "5. O que é ransomware?",
            "alternativas": [
                "Um tipo de firewall",
                "Um vírus que rouba senhas",
                "Um software que sequestra dados e exige pagamento",
                "Um tipo de backup em nuvem"
            ],
            "correta": 2
        },
        {
            "pergunta": "6. Qual é a principal função de um antivírus?",
            "alternativas": [
                "Tornar a internet mais rápida",
                "Bloquear anúncios em sites",
                "Detectar e remover softwares maliciosos",
                "Armazenar senhas com segurança"
            ],
            "correta": 2
        },
        {
            "pergunta": "7. O que caracteriza um ataque de engenharia social?",
            "alternativas": [
                "Invasão por meio de software espião",
                "Uso de força bruta para quebrar senhas",
                "Manipulação psicológica para enganar usuários",
                "Instalação remota de vírus via rede"
            ],
            "correta": 2
        },
        {
            "pergunta": "8. Qual dessas atitudes é insegura?",
            "alternativas": [
                "Verificar a autenticidade de e-mails suspeitos",
                "Usar senhas diferentes para cada site",
                "Manter o sistema atualizado",
                "Compartilhar senhas com colegas de trabalho"
            ],
            "correta": 3
        },
        {
            "pergunta": "9. O que é um gerenciador de senhas?",
            "alternativas": [
                "Um programa para apagar cookies",
                "Uma ferramenta que guarda e cria senhas seguras",
                "Um software antivírus gratuito",
                "Um firewall para redes públicas"
            ],
            "correta": 1
        },
        {
            "pergunta": "10. O que significa HTTPS em um endereço de site?",
            "alternativas": [
                "Site com acesso limitado",
                "Site hospedado fora do país",
                "Site seguro com criptografia de dados",
                "Site com links patrocinados"
            ],
            "correta": 2
        }
    ]

    respostas_usuario = []
    indice = [0]

    # Frame do questionário
    frame = ctk.CTkFrame(container)
    frame.grid(row=0, column=0, sticky="nsew")

    titulo = ctk.CTkLabel(frame, text="Quiz de Segurança Digital", font=("Arial", 24, "bold"))
    titulo.pack(pady=20)

    pergunta_label = ctk.CTkLabel(frame, text="", font=("Arial", 16), wraplength=700, justify="center")
    pergunta_label.pack(pady=10)

    alternativas_frame = ctk.CTkFrame(frame)
    alternativas_frame.pack(pady=10)

    resultado_frame = ctk.CTkFrame(frame)

    def mostrar_pergunta():
        for w in alternativas_frame.winfo_children():
            w.destroy()
        i = indice[0]
        if i < len(perguntas):
            p = perguntas[i]
            pergunta_label.configure(text=p["pergunta"])
            for idx, alt in enumerate(p["alternativas"]):
                btn = ctk.CTkButton(
                    alternativas_frame,
                    text=alt,
                    width=600,
                    fg_color="red",
                    hover_color="#aa0000",
                    command=partial(responder, idx)
                )
                btn.pack(pady=5)
        else:
            mostrar_resultado()

    def responder(escolha):
        respostas_usuario.append(escolha)
        indice[0] += 1
        mostrar_pergunta()

    def mostrar_resultado():
        alternativas_frame.pack_forget()
        pergunta_label.pack_forget()
        titulo.configure(text="Resultado")
        acertos = sum(1 for i, r in enumerate(respostas_usuario) if r == perguntas[i]["correta"])
        total = len(perguntas)
        perc = acertos / total * 100

        texto = f"✅ Você acertou {acertos} de {total} perguntas\n📊 Desempenho: {perc:.1f}%\n\n📌 Gabarito:\n"
        for i, p in enumerate(perguntas):
            correta = p["alternativas"][p["correta"]]
            texto += f"{i+1}. {correta}\n"

        resultado_label = ctk.CTkLabel(
            resultado_frame,
            text=texto,
            font=("Arial", 14),
            wraplength=700,
            justify="left"
        )
        resultado_label.pack(pady=10)
        resultado_frame.pack(pady=20)

    mostrar_pergunta()

    ctk.CTkButton(frame, text="Voltar", command=voltar, fg_color="red", width=200).pack(pady=20)
    return frame
