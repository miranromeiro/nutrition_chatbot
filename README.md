# Chatbot de Nutrição

Este é um projeto de um chatbot especialista em Nutrição. O chatbot utiliza técnicas de TF-IDF e Similaridade Cosseno para selecionar a resposta mais adequada a partir de uma base de conhecimento pré-definida.

## Estrutura do Projeto

- **main.py**: Ponto de entrada da aplicação.
- **chatbot/**: Contém a lógica do chatbot.
  - **backend.py**: Processamento da entrada e cálculo de similaridade.
  - **interface.py**: Interface gráfica com Tkinter.
- **data/knowledge_base.py**: Base de conhecimento com perguntas e respostas sobre Nutrição.
- **README.md**: Este arquivo.

## Como Executar

1. Certifique-se de ter o Python instalado.
2. Instale as dependências:
   - O Tkinter geralmente já vem com o Python.
   - Instale o scikit-learn via pip:
   
     ```
      pip install scikit-learn
     ```
   - Instale o SpeechRecognition e PyAudio via pip:  
     ```
      pip install SpeechRecognition
     ```
     ```
      pip install PyAudio
     ```
3. Execute o aplicativo:

