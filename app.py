import pandas as pd
import streamlit as st

st.set_page_config(page_title="Brecha de género · Chile", page_icon="📊", layout="wide")

df = pd.read_csv("data/casen_limpio.csv")

st.title("📊 Brecha de género en el mercado laboral chileno")
st.write(
    "Este dashboard muestra las principales diferencias entre hombres y mujeres "
    "en el mercado laboral chileno, usando datos simulados basados en la Encuesta CASEN 2022."
)

st.sidebar.header("Filtros")
regiones = st.sidebar.multiselect(
    "Región",
    options=sorted(df["region"].unique()),
    default=sorted(df["region"].unique()),
)
df = df[df["region"].isin(regiones)]

st.header("Indicadores clave")

ocupados = df[df["ocupado"] == True]
tasa = df.groupby("genero")["ocupado"].mean() * 100
ingreso = ocupados.groupby("genero")["ingreso_mensual"].median()
brecha = (ingreso["Hombre"] - ingreso["Mujer"]) / ingreso["Hombre"] * 100

col1, col2, col3 = st.columns(3)
col1.metric("Tasa ocupación Hombres", f"{tasa['Hombre']:.1f}%")
col2.metric("Tasa ocupación Mujeres", f"{tasa['Mujer']:.1f}%")
col3.metric("Brecha salarial (mediana)", f"{brecha:.1f}%")

st.header("Tasa de ocupación por género")
st.bar_chart(tasa)

st.header("Ingreso mediano por género")
st.bar_chart(ingreso)

st.header("Ingreso mediano por nivel educativo y género")
tabla_edu = ocupados.groupby(["nivel_educacion", "genero"])["ingreso_mensual"].median().unstack()
st.bar_chart(tabla_edu)

st.header("Brecha salarial por región (%)")
tabla_region = ocupados.groupby(["region", "genero"])["ingreso_mensual"].median().unstack()
tabla_region["brecha_%"] = (tabla_region["Hombre"] - tabla_region["Mujer"]) / tabla_region["Hombre"] * 100
tabla_region = tabla_region.sort_values("brecha_%")
st.bar_chart(tabla_region["brecha_%"])

st.markdown("---")
st.caption(
    "Datos simulados con base en CASEN 2022. "
    "Proyecto académico para una postulación a máster en Ciencia de Datos Aplicada a las Ciencias Sociales."
)
