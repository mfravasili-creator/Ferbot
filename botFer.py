import streamlit as st

# Configuración de la página web (Look "Tech" Negro y Verde)
st.set_page_config(page_title="AI Chatbot - Fer", page_icon="🤖", layout="centered")

st.title("🤖 Asistente Virtual 2.0")
st.subheader("Propuesta de Automatización para Fer")
st.write("Escribile al bot para probar cómo respondería con tus clientes en vivo.")


# Lógica del Cerebro del Bot en Python
def responder_cliente(mensaje_recibido):
    mensaje = mensaje_recibido.lower()

    if "hola" in mensaje or "buenas" in mensaje or "inicio" in mensaje:
        return (
            "¡Hola! Soy el asistente virtual de Fer. 👋\n\n"
            "¿En qué te puedo ayudar hoy? Escribí una de estas palabras clave:\n\n"
            "• **INFO** (Para saber qué hacemos)\n"
            "• **PRECIOS** (Para ver el catálogo básico)\n"
            "• **HORARIOS** (Para saber cuándo atendemos)\n"
            "• **HUMANO** (Para hablar directo con Fer)"
        )
    elif "info" in mensaje or "que hacen" in mensaje:
        return (
            "🚀 Nos dedicamos a potenciar emprendimientos locales con soluciones a medida.\n\n"
            "Si querés ver nuestros servicios, escribí **PRECIOS**."
        )
    elif "precio" in mensaje or "catalogo" in mensaje or "costo" in mensaje:
        return (
            "💰 **Catálogo de Servicios Iniciales:**\n\n"
            "1. Consultoría Express: $XXXX\n"
            "2. Pack Emprendedor Inicial: $XXXX\n\n"
            "📦 ¡Consultá por planes personalizados! Escribí **HUMANO** para coordinar."
        )
    elif "horario" in mensaje or "donde estan" in mensaje or "abierto" in mensaje:
        return (
            "🕒 **Horarios de atención:**\n\n"
            "Lunes a Viernes de 09:00 a 18:00 hs.\n\n"
            "¡Dejanos tu consulta que te responderemos lo antes posible!"
        )
    elif "humano" in mensaje or "fer" in mensaje or "contacto" in mensaje:
        return "Perfecto. Te estoy derivando con Fer para que te atienda personalmente. Desconectando bot... 📴"
    else:
        return (
            "🤔 No entendí bien esa opción.\n\n"
            "Por favor, escribí una de estas palabras clave: **HOLA, INFO, PRECIOS, HORARIOS o HUMANO**."
        )


# Caja de texto para que el cliente (o Fer) chatee en la web
cliente_input = st.text_input("Escribí tu mensaje acá abajo y presioná Enter:", placeholder="Ej: Hola")

# Cuando se escribe algo, el bot responde en la pantalla de la web
if cliente_input:
    st.markdown("---")
    st.markdown(f"**🧑 Cliente:** {cliente_input}")
    respuesta_bot = responder_cliente(cliente_input)
    st.info(f"**🤖 Bot:** {respuesta_bot}")