from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from data.knowledge_base import perguntas, respostas
import speech_recognition as sr

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(perguntas)

def responder(pergunta_usuario):
    """
    Processa a pergunta do usuário e retorna a resposta mais relevante,
    ou uma resposta genérica se a similaridade for baixa.
    """
    pergunta_vec = vectorizer.transform([pergunta_usuario])
    similaridades = cosine_similarity(pergunta_vec, X)
    score_max = similaridades.max()

    if score_max < 0.3:
        return "Desculpe, não entendi sua pergunta. Pode reformular com termos relacionados à nutrição ou fitness?"
    
    indice = similaridades.argmax()
    
    grupo = indice // 3
    if grupo < len(respostas):
        return respostas[grupo]
    else:
        return "Ainda não tenho informações sobre esse assunto específico."

def ouvir_microfone():
    reconhecedor = sr.Recognizer()

    with sr.Microphone() as fonte:
        print("Diga algo...")
        reconhecedor.adjust_for_ambient_noise(fonte)  # Reduz ruído
        audio = reconhecedor.listen(fonte)

        try:
            texto = reconhecedor.recognize_google(audio, language="pt-BR")
            print("Você disse: " + texto)
            return texto
        except sr.UnknownValueError:
            print("Não entendi o que você disse")
            return ""
        except sr.RequestError as e:
            print("Erro ao conectar ao serviço; {0}".format(e))
            return ""