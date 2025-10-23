"""
Esta parte es la gestion de la llamada de distintos modelos

Samir estuvo aqui
Ian apesta
"""


#Modelo de Resumen de textos (Text Summarization)
def summary(archivo):
    from transformers import pipeline

    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    #Recoger texto de ficheros
    
    return ""

#Modelo de texto a audio (text-to-speech)
def textSpeech(texto):
    return ""

#Modelo de traduccion (translation)
def translation(texto):
    return ""

#Modelo de preguntas (Question-Answering)
def questionAnswer(question):
    return ""
