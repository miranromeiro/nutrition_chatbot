import tkinter as tk
from chatbot import backend

def enviar():
    pergunta = entrada.get()
    resposta = backend.responder(pergunta)
    chat.insert(tk.END, "Você: " + pergunta + "\n")
    chat.insert(tk.END, "Bot: " + resposta + "\n\n")
    entrada.delete(0, tk.END)

def run_chatbot():
    janela = tk.Tk()
    janela.title("Chatbot de Nutrição")
    
    global chat, entrada
    chat = tk.Text(janela, height=20, width=60)
    chat.pack(padx=10, pady=10)
    
    entrada = tk.Entry(janela, width=60)
    entrada.pack(padx=10, pady=10)
    
    botao = tk.Button(janela, text="Enviar", command=enviar)
    botao.pack(pady=5)
    
    janela.mainloop()

if __name__ == "__main__":
    run_chatbot()
