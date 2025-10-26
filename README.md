PRUEBA TÉCNICA - ANALISTA DE DATOS

Autor: Anyelo Lara
Ubicación de archivos: C:\Users\ANYELO\Documents\PRUEBA TECNICA - ANALISTA DE DATOS\

PRUEBA TECNICA - ANALISTA DE DATOS/
│
├── ARCHIVOS/
│   ├── Prueba te╠ücnica analista de datos - Puntored.pdf
│   └── ventas_operadores.csv
│
├── 1. PREGUNTAS TEÓRICAS/
│   └── respuestas.md
│
├── 2. SQL/
│   └── ejercicios_sql.ipynb
│
├── 3. PYTHON/
│   └── ejercicios_python.ipynb
│
└── 4. TABLEAU/
    ├── construcción_bd.py
    ├── DASHBOARD.png
    ├── DASHBOARD.twbx
    └── ventas_ciudades.csv    
    

ADESCRIPCIÓN GENERAL

Este proyecto corresponde al desarrollo completo de una prueba técnica para el cargo de Analista de Datos.
Incluye desde la resolución de preguntas teóricas hasta la implementación práctica en SQL, Python y Tableau.

El objetivo fue analizar, procesar y visualizar datos siguiendo buenas prácticas de análisis, modelado y comunicación de resultados.

PREGUNTAS TEÓRICAS

Archivo: 1. PREGUNTAS TEÓRICAS/respuestas.md
Contiene las respuestas estructuradas a las preguntas sobre fundamentos de datos, modelado, KPIs y buenas prácticas analíticas.

SQL
Archivo: 2. SQL/ejercicios_sql.ipynb
Contiene:
Creación de bases de datos.
Inserción de datos simulados.
Consultas para obtención de métricas.
Validaciones lógicas y agrupaciones.
Las consultas fueron desarrolladas y probadas en MySQL Workbench.

PYTHON
Archivo: 3. PYTHON/ejercicios_python.ipynb
Incluye:
Carga y limpieza del dataset original (ventas_operadores.csv).
Análisis exploratorio y cálculos estadísticos.
Correlaciones, tendencias y visualizaciones.
Exportación de resultados a CSV.

Bibliotecas utilizadas:
pandas
numpy
matplotlib
seaborn
scipy.stats

Resultado principal: Coeficiente de correlación de Pearson = 0.9025, indicando una alta relación entre las variables analizadas.

TABLEAU
Archivos:
construcción_bd.py: Script que genera el dataset simulado ventas_ciudades.csv.
ventas_ciudades.csv: Dataset resultante para Tableau.
DASHBOARD.twbx: Archivo empaquetado del dashboard.
DASHBOARD.png: Imagen del dashboard final.
Componentes principales del Dashboard:
Gráfico de barras con ventas por ciudad.
Gráfico de línea temporal con la evolución de las ventas.
Indicadores de totales y promedio de ventas.
Filtro dinámico por rango de fechas configurado como deslizador (slider).

REQUERIMIENTOS DEL ENTORNO
Archivo: requirements.txt

pandas
numpy
matplotlib
seaborn
scipy

Versión recomendada de Python: 3.11 o superior.

EJECUCIÓN DEL PROYECTO
Clonar el repositorio:
git clone https://github.com/AnyeloLara/PRUEBA-T-CNICA---ANALISTA-DE-DATOS.git

Entrar en la carpeta del proyecto:
cd "PRUEBA TÉCNICA - ANALISTA DE DATOS"

Instalar las dependencias:
pip install -r requirements.txt

Ejecutar el script de construcción de la base de datos:
python "4. TABLEAU/construcción_bd.py"

Esto generará el archivo ventas_ciudades.csv, que luego se puede importar a Tableau.

RESUMEN DE RESULTADOS
SQL: Consultas funcionales y optimizadas.
Python: Análisis estadístico y correlacional completo.
Tableau: Dashboard interactivo con filtros dinámicos.
Estructura modular: Cada fase separada y documentada.

CONTACTO
Correo: edgar.larah1307@gmail.com
Ubicación: Bogotá, Colombia
GitHub: https://github.com/AnyeloLara

NOTA

Proyecto desarrollado con fines de evaluación técnica para el rol de Analista de Datos.