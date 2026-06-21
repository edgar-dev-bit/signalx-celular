import streamlit as st
from google import genai

# Coloca tu API Key real de Gemini aquí dentro de las comillas
API_KEY = "AQ.Ab8RN6IPSkPpwm_l9PIxbMOirsQQa6Ey9LSQB4dNDuoPR5uy1w"

# Configuración especial para que se adapte perfecto al celular
st.set_page_config(page_title="SignalX 5M", layout="centered", initial_sidebar_state="collapsed")

# Estilos visuales para pantalla móvil (Botones grandes y alertas claras)
st.markdown("""
    <style>
    .stButton>button { width: 100%; height: 55px; font-size: 18px; font-weight: bold; background-color: #0066cc; color: white; border-radius: 10px; }
    .big-font { font-size:20px !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("📱 SignalX — Cabina 5M")
st.write("Checklist táctico de alta precisión para operaciones de continuidad.")

def inicializar_ia():
    if API_KEY == "TU_API_KEY_AQUÍ" or not API_KEY:
        st.error("❌ Falta configurar la API Key de Gemini en el código.")
        return None
    return genai.Client(api_key=API_KEY)

client = inicializar_ia()

if client:
    # Contenedor del formulario móvil
    with st.form("mobile_trade_form"):
        st.markdown("<p class='big-font'>🎯 Tipo de Operación</p>", unsafe_allow_html=True)
        tipo_op = st.radio("Selecciona tu dirección:", ["CALL 🟢 (Compra)", "PUT 🔴 (Venta)"], horizontal=True)
        
        st.markdown("---")
        st.markdown("<p class='big-font'>👀 Checklist del Gráfico (5 min)</p>", unsafe_allow_html=True)
        
        st_val = st.selectbox("1. SuperTrend (El Tren)", ["Diagonal Limpia / Reciente", "Recto / Plano", "Tendencia Vieja (+5 velas)"])
        adx_val = st.number_input("2. Valor del ADX:", min_value=0, max_value=100, value=28)
        adx_dir = st.selectbox("3. Dirección de punta ADX", ["Subiendo (Hacia el cielo)", "Plano", "Bajando"])
        vol_val = st.selectbox("4. Volumen de la vela", ["Armónico (Un poco mayor)", "Menor que el anterior", "Gigante (Clímax)"])
        vel_ha = st.selectbox("5. Vela Heikin Ashi", ["Estructura Perfecta (Lado plano)", "Mechas en ambos lados / Cuerpo chico"])
        
        st.markdown("---")
        st.markdown("<p class='big-font'>🚨 FILTRO REAL (Pocket Option)</p>", unsafe_allow_html=True)
        precio_real = st.selectbox(
            "¿Dónde está parado el precio real vivo?", 
            ["En la punta extrema (A favor del trade)", "Atrapada en el medio del cuerpo", "Atrás (En contra del trade)"]
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        boton_validar = st.form_submit_button("VALIDAR SEÑAL EN VIVO 🚀")

    if boton_validar:
        op_limpia = "CALL" if "CALL" in tipo_op else "PUT"
        
        # Prompt optimizado para respuestas cortas y contundentes legibles en celular
        prompt = f"""
        Actúa como un validador militar y ultra estricto de opciones binarias para la estrategia Heikin Ashi 5m.
        Analiza estos datos ingresados desde el celular del trader:
        - Operación: {op_limpia}
        - SuperTrend: {st_val}
        - ADX: {adx_val} ({adx_dir})
        - Volumen: {vol_val}
        - Vela HA: {vel_ha}
        - Precio Real: {precio_real}

        Reglas de rechazo inmediato:
        1. Si SuperTrend es recto o viejo -> Rechazar.
        2. Si ADX < 25 o no está subiendo -> Rechazar.
        3. Si volumen es menor o gigante -> Rechazar.
        4. Si la vela HA no es perfecta -> Rechazar.
        5. SI EL PRECIO REAL ESTÁ EN EL MEDIO O ATRÁS -> RECHAZAR INMEDIATAMENTE (Trampa de promedio).

        Devuelve un reporte extremadamente corto (máximo 4 líneas) para pantalla móvil.
        Termina OBLIGATORIAMENTE con una sola línea en mayúsculas que diga:
        "ACCION: EJECUTAR {op_limpia}" o "ACCION: RECHAZAR / ESPERAR".
        """
        
        with st.spinner("Filtrando trampas institucionales..."):
            try:
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                )
                st.markdown("---")
                st.subheader("🎯 Veredicto de la IA")
                
                # Resaltar el veredicto para verlo sin esfuerzo en la calle
                texto_ia = response.text
                if "EJECUTAR" in texto_ia:
                    st.success(texto_ia)
                else:
                    st.error(texto_ia)
                    
            except Exception as e:
                st.error(f"Error de conexión: {e}")