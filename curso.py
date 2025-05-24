import customtkinter as ctk

def criar_curso(container, voltar):
    frame = ctk.CTkFrame(container)
    frame.grid(row=0, column=0, sticky="nsew")

    titulo = ctk.CTkLabel(frame, text="Curso - Lógica de Programação", font=("Arial", 24, "bold"))
    titulo.pack(pady=20)

    scroll_frame = ctk.CTkScrollableFrame(frame, width=800, height=500)
    scroll_frame.pack(pady=10, padx=20, fill="both", expand=True)

    # Lista para armazenar os widgets de texto
    texto_widgets = []

    def adicionar_secao(titulo_secao, conteudo):
        lbl_titulo = ctk.CTkLabel(scroll_frame, text=titulo_secao, font=("Arial", 18, "bold"))
        lbl_texto = ctk.CTkLabel(scroll_frame, text=conteudo, font=("Arial", 14), justify="left", wraplength=760)
        lbl_titulo.pack(anchor="w", pady=(15, 5))
        lbl_texto.pack(anchor="w")
        texto_widgets.append((lbl_titulo, lbl_texto))

    # Adiciona seções (resumido para exemplo)
    adicionar_secao("1. Introdução à Lógica de Programação",
    "- Conceito de lógica\n- Raciocínio lógico aplicado à programação\n- O que é algoritmo?")

    adicionar_secao("2. Algoritmos e Pseudocódigo",
    "- Definição de algoritmo\n- Representações: linguagem natural, pseudocódigo, fluxograma")

    adicionar_secao("Aula 3: Variáveis e Tipos de Dados",
                    "Variável é um espaço na memória que guarda um valor temporário.\n"
                    "É como uma 'caixa' onde armazenamos informações.\n\n"
                    "Tipos mais comuns:\n"
                    "- Inteiro: números inteiros (ex: 10, -5)\n"
                    "- Real/Float: números com vírgula (ex: 3.14, -2.5)\n"
                    "- Caractere: letras ou símbolos (ex: 'a', '$')\n"
                    "- Lógico/Booleano: verdadeiro (V) ou falso (F)")

    adicionar_secao("Aula 4: Operadores",
                    "Operadores Aritméticos:\n"
                    "+ (soma), - (subtração), * (multiplicação), / (divisão), % (resto da divisão)\n\n"
                    "Operadores Relacionais:\n"
                    "== (igual), != (diferente), > (maior), < (menor), >= (maior ou igual), <= (menor ou igual)\n\n"
                    "Operadores Lógicos:\n"
                    "AND (E) – verdadeiro se ambos forem verdadeiros\n"
                    "OR (OU) – verdadeiro se pelo menos um for verdadeiro\n"
                    "NOT (NÃO) – inverte o valor lógico")

    adicionar_secao("Aula 5: Estruturas Condicionais",
                    "Permite decisões no código com base em condições.\n\n"
                    "Exemplo:\n"
                    "se idade ≥ 18 então\n"
                    "  mostrar \"Você é maior de idade\"\n"
                    "senão\n"
                    "  mostrar \"Você é menor de idade\"\n"
                    "fim se")

    adicionar_secao("Aula 6: Estruturas de Repetição (Laços)",
                    "Permite repetir um bloco de código várias vezes.\n\n"
                    "Enquanto (while):\n"
                    "  enquanto contador < 5 faça\n"
                    "    mostrar contador\n"
                    "    contador ← contador + 1\n"
                    "  fim enquanto\n\n"
                    "Para (for):\n"
                    "  para i de 1 até 10 faça\n"
                    "    mostrar i\n"
                    "  fim para")

    adicionar_secao("Aula 7: Funções e Modularização",
                    "Funções são blocos de código com tarefas específicas.\n"
                    "Vantagens:\n"
                    "- Organização\n"
                    "- Reutilização\n"
                    "- Manutenção facilitada\n\n"
                    "Exemplo:\n"
                    "função somar(a, b)\n"
                    "  retorno a + b\n"
                    "fim função")

    # Botão de voltar
    ctk.CTkButton(frame, text="Voltar", command=voltar, fg_color="red", width=200).pack(pady=15)

    # Função para redimensionar fontes
    def ajustar_fonte(event):
        largura = event.width
        base_tamanho = max(12, int(largura / 60))  # Ajuste aqui o divisor para controlar o "zoom"
        titulo.configure(font=("Arial", base_tamanho + 10, "bold"))
        for lbl_titulo, lbl_texto in texto_widgets:
            lbl_titulo.configure(font=("Arial", base_tamanho + 4, "bold"))
            lbl_texto.configure(font=("Arial", base_tamanho))

    frame.bind("<Configure>", ajustar_fonte)

    return frame
