from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from data.knowledge_base import perguntas, respostas

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(perguntas)

def responder(pergunta_usuario):
    """
    Processa a pergunta do usuário e retorna a resposta mais relevante.
    """
    pergunta_vec = vectorizer.transform([pergunta_usuario])
    similaridades = cosine_similarity(pergunta_vec, X)
    indice = similaridades.argmax()
    return respostas[indice]
