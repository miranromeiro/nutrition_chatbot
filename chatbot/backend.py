from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from data.knowledge_base import perguntas, respostas
import speech_recognition as sr
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from deep_translator import GoogleTranslator

# Inicializações
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(perguntas)

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()


def analisar_sentimento(texto):
    traducao = GoogleTranslator(source='pt', target='en').translate(texto)
    resultado = sia.polarity_scores(traducao)
    compound = resultado['compound']

    if compound >= 0.05:
        return "positivo"
    elif compound <= -0.05:
        return "negativo"
    else:
        return "neutro"


def responder(pergunta_usuario):
    """
    Processa a pergunta do usuário, analisa o sentimento (internamente)
    e retorna a resposta mais relevante, ajustada com base no sentimento.
    """
    sentimento = analisar_sentimento(pergunta_usuario)

    pergunta_vec = vectorizer.transform([pergunta_usuario])
    similaridades = cosine_similarity(pergunta_vec, X)
    score_max = similaridades.max()

    if score_max < 0.3:
        return "Desculpe, não entendi sua pergunta. Pode reformular com termos relacionados à nutrição ou fitness?"

    indice = similaridades.argmax()
    grupo = indice // 3

    if grupo < len(respostas):
        resposta = respostas[grupo]
    else:
        resposta = "Ainda não tenho informações sobre esse assunto específico."

    # Ajuste emocional (sem mostrar para o usuário)
    if sentimento == "negativo":
        resposta = "Sinto muito que esteja se sentindo assim. " + resposta
    elif sentimento == "positivo":
        resposta = "Fico feliz em ouvir isso! " + resposta

    return resposta
    reconhecedor = sr.Recognizer()

    with sr.Microphone() as fonte:
        print("Diga algo...")
        reconhecedor.adjust_for_ambient_noise(fonte)
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
