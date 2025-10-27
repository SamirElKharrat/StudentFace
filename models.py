"""
Esta parte es la gestion de la llamada de distintos modelos

Samir estuvo aqui
"""
from transformers import pipeline
import numpy as np
from pypdf import PdfReader, errors




#Modelo de Resumen de textos (Text Summarization) y Modelo de traducción (Translate)
def summary(fichero, cantidad, idioma1, idioma2, traducir):

    idiomas = {
        "Español": "es",
        "Inglés" : "en",
        "Alemán" : "de"
    }

    summarizer = pipeline("summarization", model="Falconsai/text_summarization")

    print(fichero)
    #Recoger texto de ficheros
    try:
        reader = PdfReader(fichero)
        texto = reader.pages[0].extract_text()
        print(texto)
    except errors.PdfReadError:
        return "Solo se aceptan Pdf's."
    else:
        pass

    result = summarizer(texto, max_length=len(texto), min_length=cantidad, do_sample=False) 

    if traducir:
        textoPipe = "translation_" + idiomas[idioma1] + "_to_" + idiomas[idioma2]
        textoModel = "Helsinki-NLP/opus-mt-" + idiomas[idioma1] + "-" + idiomas[idioma2]

        traductor = pipeline(textoPipe, model=textoModel)

        traduct = traductor(texto)[0]['translation_text']

        return traduct

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

