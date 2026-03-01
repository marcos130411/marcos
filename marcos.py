import streamlit as st
import pandas as pd

st.title("Examen de Futbol")
st.write("Buena suerte, que saques buena nota. (Cada fallo resta 0,25).")

# ------------------ PREGUNTAS ------------------
preguntas = [
    {
        "texto": "¿Cuántos jugadores tiene un equipo en el campo durante un partido oficial?",
        "opciones": ["9", "10", "11", "12"],
        "correcta": "11"
    },
    {
        "texto": "¿Qué selección ganó el Mundial de 2010?",
        "opciones": ["Brasil", "Alemania", "España", "Argentina"],
        "correcta": "España"
    },
    {
        "texto": "¿En qué país juega el FC Barcelona?",
        "opciones": ["Italia", "España", "Francia", "Portugal"],
        "correcta": "España"
    },
    {
        "texto": "¿Cuántos minutos dura un partido de fútbol (sin prórroga)?",
        "opciones": ["80", "90", "100", "120"],
        "correcta": "90"
    },
    {
        "texto": "¿Qué jugador es conocido como 'La Pulga'?",
        "opciones": ["Cristiano Ronaldo", "Mbappé", "Lionel Messi", "Neymar"],
        "correcta": "Lionel Messi"
    },
    {
        "texto": "¿Qué país ha ganado más Copas del Mundo?",
        "opciones": ["Alemania", "Italia", "Argentina", "Brasil"],
        "correcta": "Brasil"
    },
    {
        "texto": "¿En qué competición se enfrentan los mejores clubes de Europa?",
        "opciones": ["Europa League", "Conference League", "Champions League", "Supercopa"],
        "correcta": "Champions League"
    },
    {
        "texto": "¿Cuántos puntos vale una victoria en liga?",
        "opciones": ["1", "2", "3", "4"],
        "correcta": "3"
    },
    {
        "texto": "¿Qué jugador ganó el Mundial 2022 con Argentina?",
        "opciones": ["Mbappé", "Modrić", "Lionel Messi", "Haaland"],
        "correcta": "Lionel Messi"
    },
 
]

# ------------------ TABS ------------------
tab_examen, tab_informe = st.tabs(["📝 Examen", "📊 Informe"])

# ------------------ TAB EXAMEN ------------------
with tab_examen:
    with st.form("quiz_form"):
        respuestas_usuario = []

        for pregunta in preguntas:
            st.subheader(pregunta["texto"])
            eleccion = st.radio(
                "Elige una opción:",
                pregunta["opciones"],
                key=pregunta["texto"]
            )
            respuestas_usuario.append(eleccion)
            st.write("---")

        boton_enviar = st.form_submit_button("Entregar Examen")

# ------------------ CORRECCIÓN ------------------
if 'boton_enviar' in locals() and boton_enviar:

    fallos = 0
    aciertos = 0
    total = len(preguntas)

    informe_md = "# 📊 Informe del Examen\n\n"

    for i in range(total):
        if respuestas_usuario[i] == preguntas[i]["correcta"]:
            aciertos += 1
            informe_md += f"✅ **{preguntas[i]['texto']}**\n"
            informe_md += f"- Tu respuesta: {respuestas_usuario[i]}\n\n"
        else:
            fallos += 1
            informe_md += f"❌ **{preguntas[i]['texto']}**\n"
            informe_md += f"- Tu respuesta: {respuestas_usuario[i]}\n"
            informe_md += f"- Respuesta correcta: {preguntas[i]['correcta']}\n\n"

    nota_base = (aciertos / total) * 10
    penalizacion = fallos * 0.25
    notafinal = round(nota_base - penalizacion, 2)
    if notafinal < 0:
        notafinal = 0

    # ------------------ MENSAJE SEGÚN NOTA ------------------
    if 1 <= notafinal <= 4:
        mensaje = "😬 Un poco flojo, ¡toca repasar!"
    elif 5 <= notafinal <= 8:
        mensaje = "🙂 Está bien, ¡pero puedes mejorar!"
        st.balloons() # ¡Efecto de globos!
    elif 9 <= notafinal <= 10:
        mensaje = "🎉 Perfecto, ¡excelente trabajo!"
        st.balloons() # ¡Efecto de globos!
    else:
        mensaje = ""

    informe_md += "---\n"
    informe_md += f"## 🎯 Nota final: {notafinal} / 10\n"
    informe_md += f"- Aciertos: {aciertos}\n"
    informe_md += f"- Fallos: {fallos}\n"
    informe_md += f"**{mensaje}**\n"

    # ------------------ TAB EXAMEN ------------------
    with tab_examen:
        st.divider()
        st.header(f"Resultado final: {notafinal} / 10")
        st.subheader(mensaje)

    # ------------------ TAB INFORME ------------------
    with tab_informe:
        st.markdown(informe_md)

        # ------------------ GRÁFICO DE RESULTADOS ------------------
        df = pd.DataFrame({
            'Resultado': ['Aciertos', 'Fallos'],
            'Cantidad': [aciertos, fallos]
        })
        st.subheader("📊 Gráfico de resultados")
        st.bar_chart(df.set_index('Resultado'))
