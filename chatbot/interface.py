import tkinter as tk
from chatbot import backend
from .reconhecimento_voz import ouvir_microfone


def enviar():
    pergunta = entrada.get()
    resposta = backend.responder(pergunta)  # Apenas 1 valor retornado
    chat.insert(tk.END, "Você: " + pergunta + "\n")
    chat.insert(tk.END, "Bot: " + resposta + "\n\n")
    entrada.delete(0, tk.END)
    chat.see(tk.END)




def enviar_por_voz():
    pergunta = ouvir_microfone()
    if pergunta:
        resposta = backend.responder(pergunta)  # Apenas 1 valor retornado
        chat.insert(tk.END, "Você (voz): " + pergunta + "\n")
        chat.insert(tk.END, "Bot: " + resposta + "\n\n")
        chat.see(tk.END)
    else:
        chat.insert(tk.END, "Bot: Desculpe, não entendi o que você disse. Tente novamente.\n\n")
        chat.see(tk.END)


def run_chatbot():
    janela = tk.Tk()
    janela.title("Chatbot de Nutrição")
    janela.configure(bg="#f0f0f0")

    header = tk.Label(
        janela, 
        text="Assistente de Nutrição", 
        font=("Arial", 16, "bold"), 
        bg="#4CAF50", 
        fg="white", 
        pady=10
    )
    header.pack(fill=tk.X)

    global chat, entrada
    chat = tk.Text(janela, height=20, width=60, bg="white", font=("Arial", 10))
    chat.pack(padx=10, pady=10)
    chat.insert(tk.END, "Bot: Olá! Sou seu assistente de nutrição. Como posso ajudar?\n\n")

    entrada = tk.Entry(janela, width=60, font=("Arial", 10))
    entrada.pack(padx=10, pady=5)

    frame_botoes = tk.Frame(janela, bg="#f0f0f0")
    frame_botoes.pack(pady=5)

    botao_enviar = tk.Button(
        frame_botoes, 
        text="Enviar", 
        command=enviar, 
        bg="#4CAF50", 
        fg="white", 
        font=("Arial", 10, "bold")
    )
    botao_enviar.pack(side=tk.LEFT, padx=5)

    botao_voz = tk.Button(
        frame_botoes, 
        text="🎤 Falar", 
        command=enviar_por_voz, 
        bg="#2196F3", 
        fg="white", 
        font=("Arial", 10, "bold")
    )
    botao_voz.pack(side=tk.LEFT, padx=5)

    entrada.focus()

    janela.bind('<Return>', lambda event: enviar())

    janela.mainloop()


if __name__ == "__main__":
    run_chatbot()

def exibir_conversa(texto):
    chat.insert(tk.END, texto + "\n")
    chat.see(tk.END)

def enviar_pergunta_voz():
    pergunta = ouvir_microfone()
    if pergunta:
        resposta, sentimento = backend.responder(pergunta)
        exibir_conversa(f"Você (voz): {pergunta}")
        exibir_conversa(f"Bot: {resposta}")
        exibir_conversa(f"[Sentimento detectado: {sentimento}]\n")