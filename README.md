# Brecha de Género en el Mercado Laboral Chileno

Este proyecto es un dashboard interactivo que analiza las desigualdades de género en el mercado laboral chileno, utilizando datos de la Encuesta CASEN 2022.

## Sobre el proyecto

Me interesa entender cómo se manifiestan las desigualdades de género en el mercado laboral chileno. Para esto, creé este dashboard que muestra:

- Tasa de ocupación por género
- Brecha salarial mediana
- Ingresos según nivel educativo y género
- Diferencias regionales en las brechas salariales

## Instalación

Necesitas Python 3.9 o superior instalado.

1. Clona el repositorio:

```bash
git clone https://github.com/kathepu/BrechaGenero.git
cd BrechaGenero
```

2. Crea un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Cómo ejecutar

```bash
streamlit run app.py
```

La aplicación se abrirá en tu navegador en `http://localhost:8501`

## Estructura del proyecto

```
BrechaGenero/
├── app.py                 # Aplicación principal de Streamlit
├── requirements.txt       # Dependencias del proyecto
├── data/
│   ├── casen_limpio.csv   # Datos procesados
│   └── casen_sintetico.csv # Datos sintéticos para demostración
├── notebooks/             # Jupyter notebooks con el análisis
└── README.md              # Este archivo
```

## Análisis realizado

El proceso incluyó:

- Carga y exploración de datos CASEN 2022
- Limpieza y transformación de variables
- Cálculo de indicadores de brecha salarial
- Agregación por región y nivel educativo

## Datos utilizados

**Fuente:** Encuesta CASEN 2022 (datos simulados basados en estructura real)

**Variables principales:**
- Género
- Tasa de ocupación
- Ingreso mensual
- Nivel educativo
- Región

## Sobre mí

Soy Katherine Paola Urdaneta Gutiérrez, Licenciada en Trabajo Social y Analista de Datos.

Contacto: kathepu@gmail.com

## Nota importante

Los datos utilizados son simulados basados en la estructura de CASEN 2022 con fines académicos. No representan datos reales.
