import streamlit as st

st.set_page_config(
    page_title="Guía de Uso - GERARD",
    page_icon="📖",
    layout="wide"
)

st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #61AFEF;
        font-size: 2.5em;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">📖 Guía de Uso de GERARD</h1>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; margin-bottom: 30px;">
    <p style="font-size: 1.2em; color: #98C379;">
        <strong>Sistema de Búsqueda Neuronal Especializado</strong><br>
        Adaptativo para Análisis de Enseñanzas del conocimiento Universal.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Cargar y mostrar el contenido de GUIA_MODELOS_PREGUNTA_GERARD.md
try:
    with open("GUIA_MODELOS_PREGUNTA_GERARD.md", "r", encoding="utf-8") as f:
        guia_content = f.read()
    
    # Mostrar contenido markdown
    st.markdown(guia_content, unsafe_allow_html=True)
    
except FileNotFoundError:
    st.error("⚠️ El archivo GUIA_MODELOS_PREGUNTA_GERARD.md no se encontró.")
    st.info("Por favor, asegúrate de que el archivo está en el directorio raíz del proyecto.")
except Exception as e:
    st.error(f"❌ Error al cargar la guía: {e}")

st.markdown("---")

# Botón para volver
if st.button("⬅️ Volver a la aplicación principal", use_container_width=True):
    st.switch_page("app_gerard.py")

st.markdown("""
<div style="text-align: center; margin-top: 40px; padding: 20px; background: rgba(97, 175, 239, 0.05); border-radius: 10px;">
    <p style="color: #98C379; font-size: 1.1em;">
        <strong>¿Tienes dudas?</strong><br>
        Contacto: arguellosolanogerardo@gmail.com
    </p>
</div>
""", unsafe_allow_html=True)
