import customtkinter as ctk
from functools import partial

def criar_questionario(container, voltar):
    container.rowconfigure(0, weight=1)
    container.columnconfigure(0, weight=1)

    frame = ctk.CTkFrame(container)
    frame.grid(row=0, column=0, sticky="nsew")

    frame.rowconfigure(1, weight=1)
    frame.columnconfigure(0, weight=1)
    perguntas = [
        {
            "pergunta": "1. O que é um algoritmo?",
            "alternativas": ["Um tipo de variável", "Uma sequência de passos para resolver um problema", "Um erro no programa", "Um comando de repetição"],
            "correta": 1
        },
        {
            "pergunta": "2. Qual tipo de dado representa valores como \"Olá\" ou \"a\"?",
            "alternativas": ["Inteiro", "Real", "Caractere", "Booleano"],
            "correta": 2
        },
        {
            "pergunta": "3. Qual operador é usado para verificar igualdade?",
            "alternativas": ["=", "!=", "==", ":="],
            "correta": 2
        },
        {
            "pergunta": "4. Em que estrutura usamos a palavra senão?",
            "alternativas": ["Repetição", "Atribuição", "Condicional", "Função"],
            "correta": 2
        },
        {
            "pergunta": "5. Qual estrutura de repetição é usada quando sabemos o número de repetições?",
            "alternativas": ["Enquanto", "Se", "Para", "Função"],
            "correta": 2
        },
        {
            "pergunta": "6. O que representa a variável em um algoritmo?",
            "alternativas": ["Um nome de função", "Um valor fixo", "Um espaço para armazenar dados", "Uma condição lógica"],
            "correta": 2
        },
        {
            "pergunta": "7. Qual operador lógico retorna verdadeiro se ao menos uma condição for verdadeira?",
            "alternativas": ["E", "NÃO", "OU", "=="],
            "correta": 2
        },
        {
            "pergunta": "8. Qual o nome da representação gráfica de um algoritmo?",
            "alternativas": ["Código", "Fluxograma", "Variável", "Comando"],
            "correta": 1
        },
        {
            "pergunta": "9. Qual é a principal vantagem de usar funções?",
            "alternativas": ["Aumentar a complexidade", "Evitar o uso de variáveis", "Organizar e reutilizar código", "Substituir operadores"],
            "correta": 2
        },
        {
            "pergunta": "10. O que acontece em um laço enquanto?",
            "alternativas": ["O código é executado apenas uma vez", "O código nunca é executado", "O código repete até a condição ser falsa", "O código executa só se a condição for falsa"],
            "correta": 2
        }
    ]

    respostas_usuario = []
    indice_pergunta = [0]

    frame = ctk.CTkFrame(container)
    frame.grid(row=0, column=0, sticky="nsew")

    titulo = ctk.CTkLabel(frame, text="Questionário", font=("Arial", 24, "bold"))
    titulo.pack(pady=20)

    pergunta_label = ctk.CTkLabel(frame, text="", font=("Arial", 16), wraplength=700, justify="center")
    pergunta_label.pack(pady=10)

    alternativas_frame = ctk.CTkFrame(frame)
    alternativas_frame.pack(pady=10)

    resultado_frame = ctk.CTkFrame(frame)

    def mostrar_pergunta():
        for widget in alternativas_frame.winfo_children():
            widget.destroy()

        i = indice_pergunta[0]
        if i < len(perguntas):
            pergunta = perguntas[i]
            pergunta_label.configure(text=pergunta["pergunta"])

            for idx, alternativa in enumerate(pergunta["alternativas"]):
                btn = ctk.CTkButton(
                    alternativas_frame,
                    text=alternativa,
                    command=partial(responder, idx),
                    width=600,
                    fg_color="red",
                    hover_color="#aa0000"
                )
                btn.pack(pady=5)
        else:
            mostrar_resultado()

    def responder(resposta_idx):
        respostas_usuario.append(resposta_idx)
        indice_pergunta[0] += 1
        mostrar_pergunta()

    def mostrar_resultado():
        alternativas_frame.pack_forget()
        pergunta_label.pack_forget()
        titulo.configure(text="Resultado")

        acertos = sum(1 for i, r in enumerate(respostas_usuario) if r == perguntas[i]["correta"])
        total = len(perguntas)
        percentual = (acertos / total) * 100

        resultado_texto = f"✅ Você acertou {acertos} de {total} perguntas\n"
        resultado_texto += f"📊 Desempenho: {percentual:.1f}%\n\n"
        resultado_texto += "📌 Gabarito:\n"
        for i, pergunta in enumerate(perguntas):
            correta = pergunta["alternativas"][pergunta["correta"]]
            resultado_texto += f"{i+1}. {correta}\n"

        resultado_texto += "\n📚 Créditos:\n"
        resultado_texto += "GUANABARA, Gustavo. Curso em Vídeo: Lógica de Programação.\n"
        resultado_texto += "https://www.cursoemvideo.com/course/curso-de-logica-de-programacao/\n"


        resultado_label = ctk.CTkLabel(
            resultado_frame,
            text=resultado_texto,
            font=("Arial", 14),
            wraplength=700,
            justify="left"
        )
        resultado_label.pack(pady=10)
        resultado_frame.pack(pady=20)

    mostrar_pergunta()

    ctk.CTkButton(frame, text="Voltar", command=voltar, fg_color="red", width=200).pack(pady=20)

    return frame
