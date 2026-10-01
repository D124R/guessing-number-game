import random
import tkinter as tk


numero_secreto = random.randint(1, 10)
tentativas = 0


def conferir_palpite(event=None):
    global tentativas

    texto = entrada.get()

    try:
        palpite = int(texto)
    except ValueError:
        mensagem.config(text="Digite um número, por favor.", fg="#b42318")
        return

    if palpite < 1 or palpite > 10:
        mensagem.config(text="Escolha um número de 1 a 10.", fg="#b42318")
        return

    tentativas += 1

    if palpite == numero_secreto:
        mensagem.config(
            text=f"Acertou em {tentativas} tentativa(s)! 🎉",
            fg="#15803d",
        )
        botao_palpite.config(state="disabled")
    elif palpite < numero_secreto:
        mensagem.config(text="Muito baixo! Tente um número maior.", fg="#475467")
    else:
        mensagem.config(text="Muito alto! Tente um número menor.", fg="#475467")

    entrada.delete(0, tk.END)
    entrada.focus_set()


def novo_jogo():
    global numero_secreto, tentativas

    numero_secreto = random.randint(1, 10)
    tentativas = 0
    mensagem.config(text="Seu número está entre 1 e 10. Boa sorte!", fg="#475467")
    botao_palpite.config(state="normal")
    entrada.delete(0, tk.END)
    entrada.focus_set()


janela = tk.Tk()
janela.title("Jogo da Adivinhação")
janela.geometry("420x360")
janela.resizable(False, False)
janela.configure(bg="#f3f4ff")

titulo = tk.Label(
    janela,
    text="🔮 Adivinhe o número!",
    font=("Arial", 22, "bold"),
    bg="#f3f4ff",
    fg="#4338ca",
)
titulo.pack(pady=(30, 8))

instrucoes = tk.Label(
    janela,
    text="Estou pensando em um número de 1 a 10.",
    font=("Arial", 12),
    bg="#f3f4ff",
    fg="#475467",
)
instrucoes.pack(pady=(0, 20))

entrada = tk.Entry(
    janela,
    font=("Arial", 20),
    justify="center",
    width=8,
    relief="flat",
)
entrada.pack(ipady=8, pady=5)
entrada.bind("<Return>", conferir_palpite)

botao_palpite = tk.Button(
    janela,
    text="Dar palpite",
    command=conferir_palpite,
    font=("Arial", 12, "bold"),
    bg="#4f46e5",
    fg="white",
    activebackground="#4338ca",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=10,
    cursor="hand2",
)
botao_palpite.pack(pady=12)

mensagem = tk.Label(
    janela,
    text="Seu número está entre 1 e 10. Boa sorte!",
    font=("Arial", 11),
    bg="#f3f4ff",
    fg="#475467",
    wraplength=360,
)
mensagem.pack(pady=8)

botao_novo_jogo = tk.Button(
    janela,
    text="Começar de novo",
    command=novo_jogo,
    font=("Arial", 10),
    bg="#e0e7ff",
    fg="#3730a3",
    relief="flat",
    padx=14,
    pady=8,
    cursor="hand2",
)
botao_novo_jogo.pack(pady=8)

entrada.focus_set()
janela.mainloop()
