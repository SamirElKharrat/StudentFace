import gradio as gr
import models as func




with gr.Blocks(title="StudentFace", css="""
body {
    background-color: #baa779;
    font-family: 'Inter', sans-serif;
    color:white;
}


#title {
    text-align: center;
    color: #0d77b5;
    font-size: 2.4em;
    font-weight: 700;
    margin-top: 10px;
}


.subtitle {
    text-align: center;
    color: white;
    font-size: 1.1em;
    margin-bottom: 25px;
}

/* Make sure rows are actually horizontal */
.gr-row {
    display: flex !important;
    flex-direction: row !important;
    justify-content: space-between;
    align-items: flex-start;
    gap: 20px;
}


.column-box {
    flex: 1 1 48%;
    background-color: #0d77b5;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.08);
}


.gr-button {
    background-color: #2563eb !important;
    color: white !important;
    border-radius: 8px !important;
}
.gr-button:hover {
    background-color: #1e40af !important;
}

""") as stface:
    

        gr.HTML("""
    <h1 id="title">🎓 StudentFace</h1>
    <p class="subtitle">Resumen, traducciones y preguntas sobre los resumenes y generación de audio.<br>Obra realizada por Ian Pagés Rodríguez y Samir El Kharrat Martín</p>
    """)
        with gr.Row():
            with gr.Column(elem_classes="column-box"):
                gr.HTML("<h3>Resumen de fichero</h3>")
                fichero = gr.File(label="Fichero a resumir")
                maxL = gr.Slider(50, 300, value=100, step=5, label="Máxima longitud del resumen.")
                gr.HTML("<h3>Traducción de texto</h3>")
                traducir = gr.Checkbox(label= "¿Quieres traducir el texto?")
                idiomaIni = gr.Dropdown(["Español","Inglés","Alemán"],label="Idioma del fichero entregado")
                idiomaFin = gr.Dropdown(["Español","Inglés","Alemán"],label="Idioma a traducir")

                btnFichero = gr.Button("Subir fichero")




                gr.HTML("<h3>Pregunta sobre el texto</h3>")
                preguntaResumen = gr.Text(label="Pregunta sobre el resumen")

                btnPregunta = gr.Button("Realizar pregunta")

                gr.HTML("<h3>Audio</h3>")
            
                btnAudio = gr.Button("Generar audio")


            with gr.Column(elem_classes="column-box"):
                gr.HTML("<h3>Resultados</h3>")
                resumen = gr.TextArea(label="Resumen")
                respuestaPregunta = gr.TextArea(label="Respuesta de la pregunta")
                AudioDelResumen = gr.Audio(label="Audio del Resumen",type="numpy")
                

        btnFichero.click(
              fn=func.summary,
              inputs=[fichero,maxL,idiomaIni,idiomaFin, traducir],
              outputs=[resumen]
        )

        btnPregunta.click(
              fn=func.questionAnswer,
              inputs=[resumen,preguntaResumen],
              outputs=[respuestaPregunta]
        )
        
        btnAudio.click(
             fn=func.textSpeech,
             inputs=[resumen],
             outputs=[AudioDelResumen]
        )



stface.launch()


