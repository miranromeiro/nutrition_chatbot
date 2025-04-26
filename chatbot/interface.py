import tkinter as tk
from chatbot import backend

def enviar():
    pergunta = entrada.get()
    resposta = backend.responder(pergunta)
    chat.insert(tk.END, "Você: " + pergunta + "\n")
    chat.insert(tk.END, "Bot: " + resposta + "\n\n")
    entrada.delete(0, tk.END)
    chat.see(tk.END)

def run_chatbot():
    janela = tk.Tk()
    janela.title("Chatbot de Nutrição")
    janela.configure(bg="#f0f0f0")
    
    header = tk.Label(janela, text="Assistente de Nutrição", font=("Arial", 16, "bold"), bg="#4CAF50", fg="white", pady=10)
    header.pack(fill=tk.X)
    
    global chat, entrada
    chat = tk.Text(janela, height=20, width=60, bg="white", font=("Arial", 10))
    chat.pack(padx=10, pady=10)
    chat.insert(tk.END, "Bot: Olá! Sou seu assistente de nutrição. Como posso ajudar?\n\n")
    
    entrada = tk.Entry(janela, width=60, font=("Arial", 10))
    entrada.pack(padx=10, pady=10)
    
    botao = tk.Button(janela, text="Enviar", command=enviar, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
    botao.pack(pady=5)
    
    entrada.focus()
    
    janela.bind('<Return>', lambda event: enviar())
    
    janela.mainloop()

if __name__ == "__main__":
    run_chatbot()
