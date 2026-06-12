# 📊 Brecha de Género en el Mercado Laboral Chileno

Dashboard interactivo que analiza las desigualdades de género en el mercado laboral chileno utilizando datos de la Encuesta CASEN 2022.

## 🎯 Descripción del Proyecto

Este proyecto examina indicadores clave de desigualdad de género incluyendo:
- **Tasa de ocupación** por género
- **Brecha salarial** mediana
- **Ingresos por nivel educativo** y género
- **Análisis regional** de brechas salariales

## 🛠️ Tecnologías Utilizadas

- **Python 3.9+**
- **Streamlit** - Framework para dashboards interactivos
- **Pandas** - Manipulación y análisis de datos
- **NumPy** - Operaciones numéricas
- **Matplotlib & Seaborn** - Visualizaciones estáticas

## 📦 Instalación

### Requisitos previos
- Python 3.9 o superior
- pip (gestor de paquetes)

### Pasos

1. Clona el repositorio:
```bash
git clone https://github.com/[TU-USUARIO]/brecha-genero-mercado-laboral.git
cd brecha-genero-mercado-laboral
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

## 🚀 Cómo ejecutar

```bash
streamlit run app.py
```

La aplicación se abrirá en tu navegador en `http://localhost:8501`

## 📊 Características principales

✅ **Filtros interactivos** por región  
✅ **Indicadores clave** en tiempo real  
✅ **Visualizaciones dinámicas** de ocupación e ingresos  
✅ **Análisis por nivel educativo**  
✅ **Comparativa regional** de brechas salariales  

## 📁 Estructura del proyecto

```
brecha-genero-mercado-laboral/
├── app.py                 # Aplicación principal de Streamlit
├── requirements.txt       # Dependencias del proyecto
├── data/
│   ├── casen_limpio.csv   # Datos procesados
│   └── casen_sintetico.csv # Datos sintéticos para demostración
└── README.md              # Este archivo
```

## 📈 Análisis realizado

### Proceso ETL
- Carga y exploración de datos CASEN 2022
- Limpieza y transformación de variables
- Cálculo de indicadores de brecha salarial
- Agregación por región y nivel educativo

### Insights principales
- Brecha salarial mediana entre géneros
- Variabilidad regional en ocupación e ingresos
- Impacto del nivel educativo en la brecha

## 📚 Datos utilizados

**Fuente:** Encuesta CASEN 2022 (datos simulados basados en estructura real)

**Variables principales:**
- Género
- Tasa de ocupación
- Ingreso mensual
- Nivel educativo
- Región

## 👥 Autor

**Katherine Paola Urdaneta Gutiérrez**  
Licenciada en Trabajo Social | Analista de Datos  
📧 kathepu@gmail.com  
🔗 LinkedIn: [Tu perfil LinkedIn]

## 📝 Licencia

Este proyecto es académico y está disponible bajo licencia MIT.

## 🤝 Contribuciones

Las sugerencias y contribuciones son bienvenidas. Por favor abre un issue o un pull request.

## ⚠️ Nota importante

Los datos utilizados son **simulados** basados en la estructura de CASEN 2022 con fines académicos. No representan datos reales.

---

**Última actualización:** 2025  
**Estado:** Completo para postulación máster
