import speech_recognition as sr

def ouvir_microfone():
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
            print("Não entendi")
            return ""
        except sr.RequestError:
            print("Erro no serviço de reconhecimento")
            return ""
