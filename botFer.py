import streamlit as st

# Configuración de la página web (Look Tech)
st.set_page_config(page_title="AI Chatbot - Fer", page_icon="🤖", layout="centered")

st.title("🤖 Asistente Virtual 2.0")
st.subheader("Propuesta de Automatización para Fer")
st.write("Escribile al bot para probar la experiencia de un chat real y fluido.")

# Lógica del Cerebro del Bot en Python
def responder_cliente(mensaje_recibido):
    mensaje = mensaje_recibido.lower()
    
    if "hola" in mensaje or "buenas" in mensaje or "inicio" in mensaje:
        return (
            "¡Hola! Soy el asistente virtual de Fer. 👋\n\n"
            "¿En qué te puedo ayudar hoy? Escribí o seleccioná una opción:\n\n"
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

# --- SISTEMA DE MEMORIA DEL CHAT ---
if "historial" not in st.session_state:
    st.session_state.historial = []

# Muestra los mensajes anteriores en la pantalla con globitos estilo WhatsApp
for mensaje in st.session_state.historial:
    with st.chat_message(mensaje["rol"]):
        st.markdown(mensaje["texto"])

# La cajita mágica de entrada que se limpia SOLA al dar Enter
if cliente_input := st.chat_input("Escribí tu mensaje acá..."):
    
    # 1. Mostrar el mensaje del usuario al toque
    with st.chat_message("user"):
        st.markdown(cliente_input)
    st.session_state.historial.append({"rol": "user", "texto": cliente_input})
    
    # 2. El bot procesa el mensaje y responde abajo
    respuesta_bot = responder_cliente(cliente_input)
    with st.chat_message("assistant"):
        st.markdown(respuesta_bot)
    st.session_state.historial.append({"rol": "assistant", "texto": respuesta_bot})
