import streamlit as st
import time

# Configuración de la página optimizada para vista móvil
st.set_page_config(
    page_title="SignalX Móvil",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilo CSS personalizado para compactar el diseño en celular
st.markdown("""
    <style>
    .block-container { padding-top: 1rem; padding-bottom: 1rem; padding-left: 0.5rem; padding-right: 0.5rem; }
    .stMetric { background-color: #1e222d; padding: 10px; border-radius: 10px; border: 1px solid #2a2e39; }
    div[data-testid="stMetricValue"] { font-size: 24px !important; font-weight: bold; }
    </style>
""", unsafe_unsafe_rendering=True)

# Encabezado compacto y gráfico
st.markdown("<h2 style='text-align: center; color: #00e676; margin-bottom: 0px;'>⚡ SIGNALX MÓVIL</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #848e9c; font-size: 14px;'>Panel Táctico de Alta Densidad</p>", unsafe_allow_html=True)

st.divider()

# --- SECCIÓN 1: PANEL DE MÉTRICAS GRÁFICAS ---
# Usamos 3 columnas bien distribuidas para que quepan en la pantalla del celular sin hacer scroll
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="⏱️ TEMP", value="1 MIN", delta="OTC", delta_color="off")

with col2:
    # Color dinámico simulado para la efectividad
    st.metric(label="🎯 EFECT.", value="87.5%", delta="+2.3%")

with col3:
    st.metric(label="📊 SEÑAL", value="CALL", delta="COMPRA", delta_color="normal")

st.markdown("<br>", unsafe_allow_html=True)

# --- SECCIÓN 2: MONITOR DE VELAS (MÁS GRÁFICO) ---
st.markdown("### 📈 Estado del Mercado")

# Barras de progreso visuales para medir la fuerza de los compradores vs vendedores
fuerza_compra = 65  # Porcentaje simulado
fuerza_venta = 35

st.markdown(f"**Fuerza de Compra (Toros): {fuerza_compra}%**")
st.progress(fuerza_compra / 100)

# --- SECCIÓN 3: BOTÓN DE ACCIÓN COMPACTO ---
st.markdown("<br>", unsafe_allow_html=True)

if st.button("🔄 ESCANEAR MERCADO EN TIEMPO REAL", use_container_width=True, type="primary"):
    with st.spinner("Analizando acción del precio..."):
        time.sleep(1.5)
        st.success("🎯 Análisis completado. Esperando confirmación de vela.")
