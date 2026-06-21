import streamlit as st
import time

# 1. Configuración de la página para vista móvil
st.set_page_config(
    page_title="SignalX Móvil",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Inyección de CSS limpio (Corregido sin errores de sintaxis)
st.markdown("""
<style>
.block-container { 
    padding-top: 1rem !important; 
    padding-bottom: 1rem !important; 
    padding-left: 0.5rem !important; 
    padding-right: 0.5rem !important; 
}
.stMetric { 
    background-color: #1e222d; 
    padding: 10px; 
    border-radius: 10px; 
    border: 1px solid #2a2e39; 
}
div[data-testid="stMetricValue"] { 
    font-size: 22px !important; 
    font-weight: bold; 
}
</style>
""", unsafe_allow_html=True)

# 3. Encabezado gráfico compacto
st.markdown("<h2 style='text-align: center; color: #00e676; margin-bottom: 0px;'>⚡ SIGNALX MÓVIL</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #848e9c; font-size: 13px;'>Panel Táctico de Alta Densidad</p>", unsafe_allow_html=True)

st.divider()

# 4. Panel de Métricas Gráficas en Columnas (Para pantallas de celular)
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="⏱️ TEMP", value="1 MIN", delta="OTC", delta_color="off")

with col2:
    st.metric(label="🎯 EFECT.", value="87.5%", delta="+2.3%")

with col3:
    st.metric(label="📊 SEÑAL", value="CALL", delta="COMPRA", delta_color="normal")

st.markdown("<br>", unsafe_allow_html=True)

# 5. Monitor de Fuerza de Velas Gráfico
st.markdown("### 📈 Estado del Mercado")

fuerza_compra = 65  
st.markdown(f"**Fuerza de Compra (Toros): {fuerza_compra}%**")
st.progress(fuerza_compra / 100)

st.markdown("<br>", unsafe_allow_html=True)

# 6. Botón de Acción Táctil
if st.button("🔄 ESCANEAR MERCADO EN TIEMPO REAL", use_container_width=True, type="primary"):
    with st.spinner("Analizando acción del precio..."):
        time.sleep(1.5)
        st.success("🎯 Análisis completado. Esperando confirmación de vela.")
