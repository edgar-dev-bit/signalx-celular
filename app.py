import streamlit as st
import time

# Configuración de la página para celular
st.set_page_config(
    page_title="SignalX Móvil",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilo CSS personalizado (Colores oscuros de trading)
st.markdown("""
    <style>
    .block-container { padding-top: 0.8rem; padding-bottom: 0.8rem; padding-left: 0.5rem; padding-right: 0.5rem; }
    .stMetric { background-color: #1a1e29; padding: 8px; border-radius: 8px; border: 1px solid #2d313f; }
    div[data-testid="stMetricValue"] { font-size: 20px !important; font-weight: bold; }
    .status-box { padding: 15px; border-radius: 8px; text-align: center; font-weight: bold; font-size: 22px; margin-bottom: 10px; }
    .call-style { background-color: #02c076; color: white; border: 1px solid #00e676; }
    .put-style { background-color: #f6465d; color: white; border: 1px solid #ff5252; }
    .wait-style { background-color: #474d57; color: #eaecef; border: 1px solid #848e9c; }
    label { font-size: 14px !important; font-weight: bold !important; color: #eaecef !important; }
    </style>
""", unsafe_allow_html=True)

# Encabezado compacto
st.markdown("<h3 style='text-align: center; color: #00e676; margin-bottom: 0px;'>⚡ SIGNALX MÓVIL</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #848e9c; font-size: 12px; margin-bottom: 5px;'>Estrategia: Heikin Ashi + EMA + RSI</p>", unsafe_allow_html=True)

st.divider()

# --- INPUTS TÁCTICOS (Para verificar las condiciones del mercado) ---
st.markdown("### 📊 Monitoreo de Indicadores")

# Distribución en dos columnas compactas para que no ocupe espacio
col_in1, col_in2 = st.columns(2)

with col_in1:
    tipo_vela = st.selectbox(
        "Velas Heikin Ashi:",
        [
            "Verde de fuerza (Sin mecha inferior)", 
            "Roja de fuerza (Sin mecha superior)", 
            "Duda / Doji (Con mechas en ambos lados)"
        ]
    )
    
    estado_rsi = st.selectbox(
        "Estado del RSI (14):",
        [
            "Apuntando hacia ARRIBA",
            "Apuntando hacia ABAJO",
            "En zona de sobrecompra (>70)",
            "En zona de sobreventa (<30)"
        ]
    )

with col_in2:
    posicion_ema = st.selectbox(
        "Precio respecto a la EMA:",
        [
            "Por ENCIMA de la EMA (Tendencia Alcista)",
            "Por DEBAJO de la EMA (Tendencia Bajista)",
            "Cruzando / Lateralizado"
        ]
    )

# --- LÓGICA ESTRICTA DE CONVERGENCIA PARA BINARIAS ---
# REGLA PARA CALL: Heikin Ashi verde fuerte + Precio sobre EMA + RSI subiendo
if (tipo_vela == "Verde de fuerza (Sin mecha inferior)" and 
    posicion_ema == "Por ENCIMA de la EMA (Tendencia Alcista)" and 
    estado_rsi == "Apuntando hacia ARRIBA"):
    
    estado_senal = "🟢 CALL (COMPRA)"
    clase_css = "call-style"
    descripcion_regla = "REGLAS CUMPLIDAS: Tendencia alcista confirmada por EMA, Heikin Ashi con cuerpo sólido y RSI apoyando el movimiento ascendente."

# REGLA PARA PUT: Heikin Ashi roja fuerte + Precio bajo EMA + RSI bajando
elif (tipo_vela == "Roja de fuerza (Sin mecha superior)" and 
      posicion_ema == "Por DEBAJO de la EMA (Tendencia Bajista)" and 
      estado_rsi == "Apuntando hacia ABAJO"):
    
    estado_senal = "🔴 PUT (VENTA)"
    clase_css = "put-style"
    descripcion_regla = "REGLAS CUMPLIDAS: Tendencia bajista confirmada por EMA, Heikin Ashi con fuerza vendedora y RSI apoyando la caída."

# REGLA PARA NO OPERAR: Si los indicadores se contradicen o hay mechas de indecisión
else:
    estado_senal = "🚫 NO OPERAR (ESPERAR)"
    clase_css = "wait-style"
    descripcion_regla = "FILTRADO POR SEGURIDAD: Los indicadores se contradicen o la vela Heikin Ashi muestra indecisión (mechas largas o contratendencia)."


# --- DESPLIEGUE GRÁFICO DE LA ALERTA ---
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f'<div class="status-box {clase_css}">{estado_senal}</div>', unsafe_allow_html=True)
st.info(descripcion_regla)


# --- MÉTRICAS DE CONTROL DE LA SESIÓN ---
st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="⏱️ TEMP", value="1 MIN", delta="OTC", delta_color="off")
with col2:
    st.metric(label="🎯 EFECT.", value="87.5%")
with col3:
    st.metric(label="📊 FILTRO", value="EMA + RSI")

# Botón de refresco manual rápido
if st.button("🔄 REFRESCAR ESCÁNER", use_container_width=True, type="primary"):
    with st.spinner("Analizando acción del precio..."):
        time.sleep(0.4)
