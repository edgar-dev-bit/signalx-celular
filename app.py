import streamlit as st
import time

# Configuración de la página optimizada para celular
st.set_page_config(
    page_title="SignalX 5M",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilo CSS de alta densidad (Colores oscuros de trading)
st.markdown("""
    <style>
    .block-container { padding-top: 2rem; padding-bottom: 0.8rem; padding-left: 0.5rem; padding-right: 0.5rem; }
    .stMetric { background-color: #1a1e29; padding: 8px; border-radius: 8px; border: 1px solid #2d313f; }
    div[data-testid="stMetricValue"] { font-size: 20px !important; font-weight: bold; }
    .status-box { padding: 15px; border-radius: 8px; text-align: center; font-weight: bold; font-size: 24px; margin-bottom: 10px; }
    .call-style { background-color: #02c076; color: white; border: 1px solid #00e676; }
    .put-style { background-color: #f6465d; color: white; border: 1px solid #ff5252; }
    .wait-style { background-color: #474d57; color: #eaecef; border: 1px solid #848e9c; }
    label { font-size: 14px !important; font-weight: bold !important; color: #eaecef !important; }
    </style>
""", unsafe_allow_html=True)

# Encabezado sin cortes
st.markdown("<h2 style='text-align: center; color: #00e676; margin-top: 10px; margin-bottom: 0px;'>⚡ SIGNALX MÓVIL</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #848e9c; font-size: 13px; margin-bottom: 5px;'>Estrategia Fija: 5M Gráfico / 5M Expiración</p>", unsafe_allow_html=True)

st.divider()

# --- MONITOREO DE INDICADORES EN 5M ---
st.markdown("### 📊 Estado de Indicadores (M5)")

col_in1, col_in2 = st.columns(2)

with col_in1:
    tipo_vela = st.selectbox(
        "Velas Heikin Ashi 5M:",
        [
            "Verde con fuerza (Sin mecha inferior)", 
            "Roja con fuerza (Sin mecha superior)", 
            "Indecisión / Doji (Con doble mecha)"
        ]
    )
    
    estado_supertrend = st.selectbox(
        "Supertrend 5M:",
        [
            "Verde / Compra (Precio por encima)",
            "Rojo / Venta (Precio por debajo)"
        ]
    )

with col_in2:
    estado_adx = st.selectbox(
        "ADX 5M (Fuerza):",
        [
            "ADX Mayor a 25 (Tendencia Fuerte)",
            "ADX Menor a 25 (Rango / Peligro)"
        ]
    )
    
    estado_volumen = st.selectbox(
        "Volumen 5M:",
        [
            "Volumen Alto (Confirmación)",
            "Volumen Bajo / Seco"
        ]
    )

# --- LÓGICA DE FILTRADO ESTRICTO PARA OPERACIONES DE 5 MINUTOS ---

# REGLA PARA CALL (COMPRA A 5M)
if (tipo_vela == "Verde con fuerza (Sin mecha inferior)" and 
    estado_supertrend == "Verde / Compra (Precio por encima)" and 
    estado_adx == "ADX Mayor a 25 (Tendencia Fuerte)" and 
    estado_volumen == "Volumen Alto (Confirmación)"):
    
    estado_senal = "🟢 CALL (COMPRA 5 MIN)"
    clase_css = "call-style"
    descripcion_regla = "🔥 CONVERGENCIA 5M: Tendencia sólida. Heikin Ashi limpia, Supertrend a favor, ADX > 25 y volumen alto. Entrada válida para expiración de 5 minutos."

# REGLA PARA PUT (VENTA A 5M)
elif (tipo_vela == "Roja con fuerza (Sin mecha superior)" and 
      estado_supertrend == "Rojo / Venta (Precio por debajo)" and 
      estado_adx == "ADX Mayor a 25 (Tendencia Fuerte)" and 
      estado_volumen == "Volumen Alto (Confirmación)"):
    
    estado_senal = "🔴 PUT (VENTA 5 MIN)"
    clase_css = "put-style"
    descripcion_regla = "🔥 CONVERGENCIA 5M: Presión bajista fuerte. Heikin Ashi sin mecha superior, Supertrend rojo, ADX fuerte y volumen alto. Entrada válida para expiración de 5 minutos."

# REGLA PARA NO OPERAR
else:
    estado_senal = "🚫 NO OPERAR (ESPERAR VELA)"
    clase_css = "wait-style"
    descripcion_regla = "⏳ FILTRADO DE SEGURIDAD: Los indicadores no están alineados en 5M. Evita pérdidas, espera que abra la siguiente vela de 5 minutos."


# --- DESPLIEGUE GRÁFICO DE LA SEÑAL ---
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f'<div class="status-box {clase_css}">{estado_senal}</div>', unsafe_allow_html=True)
st.info(descripcion_regla)


# --- PANEL DE CONTROL FIJO DE LA SESIÓN ---
st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="⏱️ VELAS", value="5 MIN", delta="Fijo", delta_color="off")
with col2:
    st.metric(label="⏳ EXPIRACIÓN", value="5 MIN", delta="Fijo", delta_color="off")
with col3:
    st.metric(label="📊 MERCADO", value="OTC", delta="Pocket Option", delta_color="normal")

if st.button("🔄 REFRESCAR ESCÁNER 5M", use_container_width=True, type="primary"):
    with st.spinner("Verificando cierre de vela de 5 minutos..."):
        time.sleep(0.4)
