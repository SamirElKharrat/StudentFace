"""
Esta parte es la gestion de la llamada de distintos modelos

Samir estuvo aqui
Ian apesta
"""
from transformers import pipeline
import numpy as np


#Modelo de Resumen de textos (Text Summarization)
def summary(archivo, cantidad):

    summarizer = pipeline("summarization", model="Falconsai/text_summarization")

    #Recoger texto de ficheros
    with open("ejemplo.txt", 'r', encoding='utf-8') as file:
        texto = file.read()

    result = summarizer(texto, max_length=200, min_length=cantidad, do_sample=False) 
    return result[0]["summary_text"]

#Modelo de texto a audio (text-to-speech)
def textSpeech(texto):
    synthesiser = pipeline("text-to-speech", "suno/bark")

    speech = synthesiser(texto, forward_params={"do_sample": True})

    audio = speech["audio"]

    if audio.ndim > 1:
          audio = np.mean(audio, axis = 0)

    audio16 = np.int16(audio* 32767)

    return (speech["sampling_rate"], audio16)

#Modelo de traduccion (translation)
def translation(texto, idioma1, idioma2):
    idiomas = {
        "Español": "es",
        "Inglés" : "en",
        "Alemán" : "de"
    }

    textoPipe = "translation_" + idiomas[idioma1] + "_to_" + idiomas[idioma2]
    textoModel = "Helsinki-NLP/opus-mt-" + idiomas[idioma1] + "-" + idiomas[idioma2]

    traductor = pipeline(textoPipe, model=textoModel)

    result = traductor(texto)[0]['translation_text']

    return result

#Modelo de preguntas (Question-Answering)
def questionAnswer(texto, question):
    qa_pipeline = pipeline(
        "question-answering",
        model="mrm8488/bert-multi-uncased-finetuned-xquadv1",
        tokenizer="mrm8488/bert-multi-uncased-finetuned-xquadv1"
    )   

    result = qa_pipeline({
        "context": texto,
        "question": question
    })

    return result["answer"]

