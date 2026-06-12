import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

st.set_page_config(page_title="Brecha de género · Chile", page_icon="📊", layout="wide")

AZUL_OSCURO  = "#1B3A6B"
AZUL_MEDIO   = "#2E5FA3"
AZUL_CLARO   = "#7B9DC9"
CREMA        = "#F5F7FA"
BLANCO       = "#FFFFFF"
GRIS_SUAVE   = "#E8EDF5"
TEXTO_OSCURO = "#1a2744"
TEXTO_SUAVE  = "#4a5a78"

st.markdown(f"""
<style>
    /* Fondo general */
    .stApp {{ background-color: {CREMA}; }}

    /* Sidebar */
    [data-testid="stSidebar"] {{
        background-color: {AZUL_OSCURO};
    }}
    [data-testid="stSidebar"] * {{
        color: {BLANCO} !important;
    }}
    [data-testid="stSidebar"] .stMultiSelect [data-baseweb="tag"] {{
        background-color: {AZUL_MEDIO} !important;
    }}
    [data-testid="stSidebar"] [data-baseweb="select"] > div {{
        background-color: #243f73 !important;
        border: 1px solid #3d5a8a !important;
        color: {BLANCO} !important;
    }}

    /* Métricas */
    [data-testid="stMetric"] {{
        background-color: {BLANCO};
        border-left: 4px solid {AZUL_MEDIO};
        border-radius: 8px;
        padding: 18px 22px;
        box-shadow: 0 2px 8px rgba(27,58,107,0.08);
    }}
    [data-testid="stMetricLabel"] {{ color: {TEXTO_SUAVE} !important; font-size: 0.85rem; }}
    [data-testid="stMetricValue"] {{ color: {AZUL_OSCURO} !important; font-weight: 700; }}

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 6px;
        background-color: transparent;
        border-bottom: 2px solid {GRIS_SUAVE};
    }}
    .stTabs [data-baseweb="tab"] {{
        background-color: {GRIS_SUAVE};
        color: {TEXTO_SUAVE};
        border-radius: 8px 8px 0 0;
        padding: 8px 20px;
        font-weight: 500;
        border: none;
        transition: opacity 0.2s ease;
    }}
    .stTabs [data-baseweb="tab"]:hover {{
        background-color: {GRIS_SUAVE} !important;
        color: {TEXTO_OSCURO} !important;
        opacity: 0.75;
    }}
    .stTabs [aria-selected="true"] {{
        background-color: {AZUL_OSCURO} !important;
        color: #ffffff !important;
        opacity: 1 !important;
        font-weight: 600 !important;
    }}
    .stTabs [aria-selected="true"] * {{
        color: #ffffff !important;
    }}
    .stTabs [aria-selected="true"]:hover {{
        background-color: {AZUL_OSCURO} !important;
        color: #ffffff !important;
        opacity: 0.9;
    }}
    .stTabs [aria-selected="true"]:hover * {{
        color: #ffffff !important;
    }}

    /* Título y texto */
    h1 {{ color: {TEXTO_OSCURO} !important; font-weight: 700; letter-spacing: -0.5px; }}
    h2, h3 {{ color: {AZUL_OSCURO}; }}
    p, .stMarkdown {{ color: {TEXTO_SUAVE}; }}

    /* Divisor */
    hr {{ border-color: {GRIS_SUAVE}; }}
</style>
""", unsafe_allow_html=True)

# Paleta para gráficos
C_HOMBRE = AZUL_OSCURO
C_MUJER  = AZUL_CLARO
C_BRECHA = AZUL_MEDIO

def estilo_grafico(ax, titulo=""):
    ax.set_facecolor(BLANCO)
    ax.figure.set_facecolor(BLANCO)
    ax.grid(axis='y', color=GRIS_SUAVE, linewidth=1, linestyle='--')
    ax.spines[['top', 'right', 'left']].set_visible(False)
    ax.spines['bottom'].set_color(GRIS_SUAVE)
    ax.tick_params(colors=TEXTO_SUAVE, labelsize=10)
    ax.set_title(titulo, fontsize=13, fontweight='600', color=AZUL_OSCURO, pad=14)
    ax.yaxis.label.set_color(TEXTO_SUAVE)
    ax.xaxis.label.set_color(TEXTO_SUAVE)

df = pd.read_csv("data/casen_limpio.csv")

# Encabezado
st.title("Brecha de género en el mercado laboral chileno")
st.markdown("Análisis de las principales diferencias entre hombres y mujeres usando datos de la Encuesta CASEN 2022.")

# Filtro horizontal (no apilado en sidebar)
st.markdown("<br>", unsafe_allow_html=True)
todas_regiones = sorted(df["region"].unique())
regiones = st.multiselect(
    "Filtrar por región",
    options=todas_regiones,
    default=todas_regiones,
    placeholder="Selecciona una o más regiones..."
)
if not regiones:
    regiones = todas_regiones

df = df[df["region"].isin(regiones)]

st.markdown("<br>", unsafe_allow_html=True)

# Indicadores
ocupados = df[df["ocupado"] == True]
tasa    = df.groupby("genero")["ocupado"].mean() * 100
ingreso = ocupados.groupby("genero")["ingreso_mensual"].median()
brecha  = (ingreso["Hombre"] - ingreso["Mujer"]) / ingreso["Hombre"] * 100

col1, col2, col3 = st.columns(3)
col1.metric("Tasa de ocupación — Hombres", f"{tasa['Hombre']:.1f}%")
col2.metric("Tasa de ocupación — Mujeres", f"{tasa['Mujer']:.1f}%")
col3.metric("Brecha salarial mediana", f"{brecha:.1f}%")

st.markdown("<br>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["  Ocupación  ", "  Ingresos  ", "  Educación  ", "  Regiones  "])

with tab1:
    fig, ax = plt.subplots(figsize=(7, 4))
    bars = ax.bar(tasa.index, tasa.values, color=[C_HOMBRE, C_MUJER], width=0.5, zorder=3)
    for b in bars:
        ax.text(b.get_x() + b.get_width()/2, b.get_height() + 0.5,
                f"{b.get_height():.1f}%", ha='center', va='bottom',
                fontsize=11, color=TEXTO_OSCURO, fontweight='600')
    ax.set_ylabel("Tasa (%)")
    ax.set_ylim(0, tasa.max() * 1.2)
    estilo_grafico(ax, "Tasa de ocupación por género")
    st.pyplot(fig)
    plt.close()

with tab2:
    fig, ax = plt.subplots(figsize=(7, 4))
    bars = ax.bar(ingreso.index, ingreso.values, color=[C_HOMBRE, C_MUJER], width=0.5, zorder=3)
    for b in bars:
        ax.text(b.get_x() + b.get_width()/2, b.get_height() + 5000,
                f"${b.get_height():,.0f}", ha='center', va='bottom',
                fontsize=10, color=TEXTO_OSCURO, fontweight='600')
    ax.set_ylabel("Ingreso mediano (CLP)")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))
    ax.set_ylim(0, ingreso.max() * 1.2)
    estilo_grafico(ax, "Ingreso mediano por género")
    st.pyplot(fig)
    plt.close()

with tab3:
    tabla_edu = ocupados.groupby(["nivel_educacion", "genero"])["ingreso_mensual"].median().unstack()
    fig, ax = plt.subplots(figsize=(11, 5))
    x = range(len(tabla_edu))
    w = 0.38
    ax.bar([i - w/2 for i in x], tabla_edu["Hombre"], width=w, label="Hombre", color=C_HOMBRE, zorder=3)
    ax.bar([i + w/2 for i in x], tabla_edu["Mujer"],  width=w, label="Mujer",  color=C_MUJER,  zorder=3)
    ax.set_xticks(list(x))
    ax.set_xticklabels(tabla_edu.index, rotation=30, ha='right', fontsize=9)
    ax.set_ylabel("Ingreso mediano (CLP)")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"${v:,.0f}"))
    legend = ax.legend(title="Género", frameon=False, labelcolor=TEXTO_SUAVE)
    legend.get_title().set_color(TEXTO_SUAVE)
    estilo_grafico(ax, "Ingreso mediano por nivel educativo")
    st.pyplot(fig)
    plt.close()

with tab4:
    tabla_region = ocupados.groupby(["region", "genero"])["ingreso_mensual"].median().unstack()
    tabla_region["brecha_%"] = (tabla_region["Hombre"] - tabla_region["Mujer"]) / tabla_region["Hombre"] * 100
    tabla_region = tabla_region.sort_values("brecha_%")
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(tabla_region.index, tabla_region["brecha_%"], color=C_BRECHA, width=0.6, zorder=3)
    ax.set_ylabel("Brecha salarial (%)")
    ax.set_ylim(0, tabla_region["brecha_%"].max() * 1.2)
    plt.xticks(rotation=40, ha='right', fontsize=9)
    estilo_grafico(ax, "Brecha salarial por región")
    st.pyplot(fig)
    plt.close()

st.markdown("<br><br>")
st.markdown(f"<p style='text-align:center; color:{TEXTO_SUAVE}; font-size:0.85rem;'>Hecho con ❤️ por Katherine Urdaneta &nbsp;·&nbsp; Datos simulados con base en CASEN 2022</p>", unsafe_allow_html=True)
