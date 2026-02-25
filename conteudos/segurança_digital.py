import customtkinter as ctk

def criar_seg_digital(container, voltar):
    frame = ctk.CTkFrame(container)
    frame.grid(row=0, column=0, sticky="nsew")

    titulo = ctk.CTkLabel(frame, text="Curso - Segurança Digital", font=("Arial", 24, "bold"))
    titulo.pack(pady=20)

    scroll_frame = ctk.CTkScrollableFrame(frame, width=800, height=500)
    scroll_frame.pack(pady=10, padx=20, fill="both", expand=True)

    texto_widgets = []

    def adicionar_secao(titulo_secao, conteudo):
        lbl_titulo = ctk.CTkLabel(scroll_frame, text=titulo_secao, font=("Arial", 18, "bold"))
        lbl_texto = ctk.CTkLabel(scroll_frame, text=conteudo, font=("Arial", 14), justify="left", wraplength=760)
        lbl_titulo.pack(anchor="w", pady=(15, 5))
        lbl_texto.pack(anchor="w")
        texto_widgets.append((lbl_titulo, lbl_texto))

    adicionar_secao("1. O que é Segurança Digital?",
        "Entenda o conceito de segurança digital, sua importância no cotidiano e por que proteger seus dados e dispositivos é fundamental na era da informação."
    )

    adicionar_secao("2. Tipos de Ameaças Digitais",
        "Phishing, Malware, Ransomware e Engenharia Social — como funcionam e como afetam usuários e empresas."
    )

    adicionar_secao("3. Boas Práticas de Segurança",
        "- Use senhas fortes e únicas\n"
        "- Ative autenticação em duas etapas\n"
        "- Mantenha software atualizado\n"
        "- Cuidado com links suspeitos\n"
        "- Faça backups regulares"
    )

    adicionar_secao("4. Navegação Segura na Internet",
        "- Use sites com HTTPS\n"
        "- Evite redes Wi-Fi públicas sem proteção\n"
        "- Configure sua privacidade nas redes sociais\n"
        "- Baixe apps apenas de lojas oficiais"
    )

    adicionar_secao("5. Segurança Digital no Trabalho",
        "- Não compartilhe senhas\n"
        "- Bloqueie o computador ao se ausentar\n"
        "- Use dispositivos da empresa apenas profissionalmente\n"
        "- Desconfie de e-mails com anexos estranhos"
    )

    adicionar_secao("6. Referências",
        "- CERT.br, SaferNet, Kaspersky, Avast, ESET"
    )

    adicionar_secao("7. Quiz de Segurança Digital",
        "Teste seus conhecimentos sobre os temas abordados."
    )

    # Aulas detalhadas
    adicionar_secao("Aula 1: O que é Segurança Digital?",
        "Segurança Digital refere-se à proteção de informações digitais, dispositivos e sistemas contra acessos não autorizados, ataques e danos.\n\n"
        "Envolve práticas, tecnologias e comportamentos que garantem a privacidade, integridade e disponibilidade dos dados.\n\n"
        "Por que é importante?\n"
        "- Protege seus dados pessoais e financeiros.\n"
        "- Evita fraudes e roubo de identidade.\n"
        "- Garante o bom funcionamento de dispositivos e redes."
    )

    adicionar_secao("Aula 2: Tipos de Ameaças Digitais",
        "- Phishing: Tentativa de enganar o usuário para obter informações sensíveis por e-mail, SMS ou redes sociais.\n"
        "- Malware: Software malicioso como vírus, worms, trojans, spyware e ransomware.\n"
        "- Ransomware: Sequestra os dados do usuário e exige pagamento para desbloqueá-los.\n"
        "- Engenharia Social: Manipulação psicológica para obter dados confidenciais.\n"
        "- Roubo de Senhas: Pode ocorrer via keyloggers, senhas fracas ou reutilização."
    )

    adicionar_secao("Aula 3: Boas Práticas de Segurança",
        "1. Senhas Fortes\n"
        "   - Use senhas longas (12+ caracteres), com letras maiúsculas, minúsculas, números e símbolos.\n"
        "   - Nunca reutilize senhas em sites diferentes.\n"
        "   - Use um gerenciador de senhas confiável.\n\n"
        "2. Autenticação em Duas Etapas (2FA)\n"
        "   - Adiciona uma camada extra de segurança usando um código enviado por SMS, e-mail ou app autenticador.\n\n"
        "3. Atualizações de Software\n"
        "   - Mantenha sistema operacional, aplicativos e antivírus sempre atualizados.\n\n"
        "4. Cuidado com e-mails e links suspeitos\n"
        "   - Verifique remetente, erros de digitação e evite clicar em links desconhecidos.\n\n"
        "5. Backups\n"
        "   - Faça cópias de segurança regulares (HD externo ou nuvem)."
    )

    adicionar_secao("Aula 4: Navegação Segura na Internet",
        "Use sites com HTTPS (cadeado ao lado do link).\n"
        "Evite redes Wi-Fi públicas para acessar dados sensíveis (use VPN se necessário).\n"
        "Configure a privacidade nas redes sociais.\n"
        "Baixe apps apenas de lojas oficiais (Google Play, App Store)."
    )

    adicionar_secao("Aula 5: Segurança Digital no Trabalho",
        "Não compartilhe senhas com colegas.\n"
        "Bloqueie o computador ao se ausentar.\n"
        "Use dispositivos da empresa apenas para fins profissionais.\n"
        "Desconfie de e-mails com anexos ou pedidos de urgência fora do padrão."
    )

    adicionar_secao("Créditos",
        "Cartilha de Segurança para Internet – CERT.br (https://cartilha.cert.br)\n"
        "Guia de Segurança Digital – SaferNet Brasil (https://www.safernet.org.br)\n"
        "Enciclopédia de Ameaças – Kaspersky\n"
        "Blog de Cibersegurança – Avast (https://www.avast.com/pt-br/cybersecurity)\n"
        "Blog de Segurança – ESET (https://www.welivesecurity.com/br/)"
    )

    ctk.CTkButton(frame, text="Voltar", command=voltar, fg_color="red", width=200).pack(pady=15)

    # Ajuste de fonte responsivo
    def ajustar_fonte(event):
        largura = event.width
        base = max(12, int(largura / 60))
        titulo.configure(font=("Arial", base + 10, "bold"))
        for lbl_t, lbl_txt in texto_widgets:
            lbl_t.configure(font=("Arial", base + 4, "bold"))
            lbl_txt.configure(font=("Arial", base))

    frame.bind("<Configure>", ajustar_fonte)

    return frame
