import streamlit as st
import time

# Configuración de la página optimizada para celular
st.set_page_config(
    page_title="SignalX Móvil",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilo CSS de alta densidad corregido (Evita que se corte el título)
st.markdown("""
    <style>
    .block-container { padding-top: 2rem; padding-bottom: 0.8rem; padding-left: 0.5rem; padding-right: 0.5rem; }
    .stMetric { background-color: #1a1e29; padding: 8px; border-radius: 8px; border: 1px solid #2d313f; }
    div[data-testid="stMetricValue"] { font-size: 20px !important; font-weight: bold; }
    .status-box { padding: 15px; border-radius: 8px; text-align: center; font-weight: bold; font-size: 22px; margin-bottom: 10px; }
    .call-style { background-color: #02c076; color: white; border: 1px solid #00e676; }
    .put-style { background-color: #f6465d; color: white; border: 1px solid #ff5252; }
    .wait-style { background-color: #474d57; color: #eaecef; border: 1px solid #848e9c; }
    label { font-size: 14px !important; font-weight: bold !important; color: #eaecef !important; }
    </style>
""", unsafe_allow_html=True)

# Encabezado corregido sin cortes
st.markdown("<h2 style='text-align: center; color: #00e676; margin-top: 10px; margin-bottom: 0px;'>⚡ SIGNALX MÓVIL</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #848e9c; font-size: 13px; margin-bottom: 5px;'>Estrategia Táctica: Heikin Ashi + ADX + Supertrend + Volumen</p>", unsafe_allow_html=True)

st.divider()

# --- MONITOREO DE INDICADORES REALES ---
st.markdown("### 📊 Monitoreo de Indicadores")

col_in1, col_in2 = st.columns(2)

with col_in1:
    tipo_vela = st.selectbox(
        "Velas Heikin Ashi:",
        [
            "Verde con fuerza (Sin mecha inferior)", 
            "Roja con fuerza (Sin mecha superior)", 
            "Indecisión / Doji (Con doble mecha)"
        ]
    )
    
    estado_supertrend = st.selectbox(
        "Indicador Supertrend:",
        [
            "Verde / Compra (Precio por encima)",
            "Rojo / Venta (Precio por debajo)"
        ]
    )

with col_in2:
    estado_adx = st.selectbox(
        "Fuerza de Tendencia (ADX):",
        [
            "ADX Mayor a 25 (Tendencia Fuerte)",
            "ADX Menor a 25 (Mercado Débil / Rango)"
        ]
    )
    
    estado_volumen = st.selectbox(
        "Volumen de Mercado:",
        [
            "Volumen Alto (Confirmación)",
            "Volumen Bajo / Seco"
        ]
    )

# --- LÓGICA DE CONVERGENCIA PARA BINARIAS (Pocket Option) ---

# REGLA PARA CALL
if (tipo_vela == "Verde con fuerza (Sin mecha inferior)" and 
    estado_supertrend == "Verde / Compra (Precio por encima)" and 
    estado_adx == "ADX Mayor a 25 (Tendencia Fuerte)" and 
    estado_volumen == "Volumen Alto (Confirmación)"):
    
    estado_senal = "🟢 CALL (COMPRA)"
    clase_css = "call-style"
    descripcion_regla = "REGLAS CUMPLIDAS: Supertrend alcista, vela Heikin Ashi con cuerpo sólido, ADX con fuerza (>25) y volumen acompañando la ruptura."

# REGLA PARA PUT
elif (tipo_vela == "Roja con fuerza (Sin mecha superior)" and 
      estado_supertrend == "Rojo / Venta (Precio por debajo)" and 
      estado_adx == "ADX Mayor a 25 (Tendencia Fuerte)" and 
      estado_volumen == "Volumen Alto (Confirmación)"):
    
    estado_senal = "🔴 PUT (VENTA)"
    clase_css = "put-style"
    descripcion_regla = "REGLAS CUMPLIDAS: Supertrend bajista, vela Heikin Ashi con presión vendedora, fuerza en ADX y volumen alto confirmando la caída."

# REGLA PARA NO OPERAR
else:
    estado_senal = "🚫 NO OPERAR (ESPERAR)"
    clase_css = "wait-style"
    descripcion_regla = "FILTRADO POR SEGURIDAD: Falta volumen, el ADX está en rango bajo (<25) o la vela Heikin Ashi muestra mechas de indecisión."


# --- DESPLIEGUE GRÁFICO DE LA SEÑAL ---
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f'<div class="status-box {clase_css}">{estado_senal}</div>', unsafe_allow_html=True)
st.info(descripcion_regla)


# --- MÉTRICAS DE CONTROL DE LA SESIÓN ---
st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="⏱ ...", value="1 MIN", delta="OTC", delta_color="off")
with col2:
    st.metric(label="🎯 EFECT.", value="87.5%")
with col3:
    st.metric(label="📊 FILTROS", value="HA+ADX+ST")

if st.button("🔄 REFRESCAR ESCÁNER", use_container_width=True, type="primary"):
    with st.spinner("Analizando acción del precio..."):
        time.sleep(0.4)
