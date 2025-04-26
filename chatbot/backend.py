from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from data.knowledge_base import perguntas, respostas

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