SQL

1. ¿Cuál es la diferencia entre un JOIN y un UNION en SQL? Proporcione un ejemplo.

La diferencia Radica en como se combinan los datos, el JOIN combina los datos de forma horizontal basado en una columna en común o llave primaria muy similar a un buscar x, mientras que UNION como lo dice la palabra, une dos tablas que tengan la misma estructura de forma vertical se usa cuando se tienen tablas similares y se necesita tener toda la información en una sola.

Ejemplo JOIN:

Tenemos dos tablas, tabla clientes (con id y nombre) y una tabla pedidos (con id_pedido, cliente_id y monto).

Quiero saber el nombre de cada cliente junto a los pedidos.

SELECT 
    clientes.nombre,
    pedidos.monto
FROM clientes
INNER JOIN pedidos 
    ON clientes.id = pedidos.cliente_id;

Ejemplo de UNION:

Tengo una tabla ventas2023 y otra ventas2024 con la mismas columnas (fecha, monto)

Las debo unir en un mismo listado.

SELECT fecha, monto FROM ventas2023
UNION ALL
SELECT fecha, monto FROM ventas2024;

2. Explique qué es una consulta CTE (Common Table Expression) y mencione un caso de uso.

Es una consulta que permite crear una tabla temporal, se define usando la cláusula WITH antes de la consulta principal y ayuda a simplificar consultas dividiendo la logica en pasos.

El caso de uso primero Calcula el promedio de ventas para cada región, luego se usa ese promedio calculado, se une la tabla de ventas con la CTE y para el final se filtra solo los que superan el promedio.

WITH PromedioVentasRegional AS (
    SELECT
        region,
        AVG(monto_venta) AS promedio_regional
    FROM
        Ventas
    GROUP BY
        region
)
SELECT
    v.nombre_vendedor,
    v.monto_venta,
    pvr.promedio_regional
FROM
    Ventas v
JOIN
    PromedioVentasRegional pvr ON v.region = pvr.region 
WHERE
    v.monto_venta > pvr.promedio_regional; 

3. ¿Qué es la cláusula HAVING en SQL y en qué se diferencia de WHERE?

La diferencia esta en el orden de ejecución dentro de la consulta que utiliza un agrupamiento (GROUP BY).

Pero el trasfondo es mas complejo ya que con WHERE se reduce el conjunto de datos de entrada antes de que se realicen los cálculos de agregación que es lo mas pesado esto hace el proceso mas eficiente, mientras que HAVING es un filtro secundario que realiza despues de los calculos y permite resumir los resultados basandose en la metrica calculada.

4. Dado el siguiente conjunto de datos en una tabla llamada ventas, escriba una consulta SQL para obtener el total de ventas por cliente, incluyendo sólo aquellos con un monto total superior a 250.

Se agrupa por cliente_id y se suman las ventas y luego con HAVING se filtran los que superaron los 250.

SELECT
    cliente_id, 
    SUM(monto) AS total_ventas 
FROM
    ventas 
GROUP BY
    cliente_id -- Agrupa las filas por el identificador del cliente
HAVING
    SUM(monto) > 250;

El resultado trae el cliente_id 101 con total_ventas 500


PYTHON

1. ¿Cuál es la diferencia entre una lista y un diccionario en Python? Dé un ejemplo de cada uno.

Ambas son variables que permiten almacenar conjuntos de datos, en la lista se almacenan bajo corchetes y cada dato tiene un orden definido estos se pueden modificar, mientras que en un diccionario se almacenan datos en pareja tipo clave valor, estos tambien tienen un orden pero se accede a ellos por la clave en el diccionario no se permite duplicados el duplicado reescribe el valor de la clave mientras que una lista si permite duplicados.

Ejemplo Lista:

CARGOS = ["GERENTE", "DIRECTOR", "ANALISTA", "ASISITENTE"]
print(CARGOS[2]) 

RESULTADO: ANALISTA

Ejemplo de Diccionario:

COLABORADORES = {"GERENCIA": 8, "DIRECCIÓN": 12, "ANALISTAS": 25, "ASISITENTES": 32}
print(COLABORADORES["ANALISTAS"])

RESULTADO: 25

2. ¿Qué librerías en Python se utilizan comúnmente para análisis de datos?

Las mas usadas son Pandas, Numpy y Matplotlib, pandas permite cargar las bases de datos que estan en excel o csv y las carga en memoria como dataframe permite hacer limpieza como filtros, agregaciones y transformaciones complejas con pocas lineas de codigo. Numpy es mas para calculos matemáticos avanzados es muy rapido y sirve de base para librerias de machine learning y Matplotlib se basa en el tema visual permite hacer graficos complejos para identificar patrones y tendencias.

3. ¿Qué salida generará el siguiente código en Python?

data = [5, 3, 9, 1]
print(sorted(data)[-2])

La Lista data contiene valores numéricos en desorden, la función sorted los organiza de forma ascendente [1, 3, 5, 9] y con el -2 elige en orden del final al inicio el segundo valor que para este caso sería 5.


TABLEAU

1. ¿Cuál es la diferencia entre una medida y una dimensión en Tableau?

Ambos son valores que contiene una tabla, la diferencia es que una medida es cuantitativa mientras que la dimensión es un atributo cualitativo, son como cuando se crea una tabla dinámica que se arrastran los numeros como total ventas a la parte de valores y digamos clientes en filas, para analizar el total de ventas de cada cliente.

2. ¿Qué tipo de gráfico es más adecuado para comparar porcentajes de una variable categórica?

Normalmente se emplearía o un grafico de barras o uno de torta dependería de la cantidad de categorías que tenga la variable, si son 3 o 4 se vería bien una de torta si son mas es mejor la de barras y dependiendo de la longitud de la categoría y la disposición en el tablero las manejaria verticales u horizontales.

3. ¿Cómo se puede crear un filtro dinámico en Tableau para que el usuario pueda seleccionar un rango de fechas?

Al igual que en una dinámica solo se arrastra el campo de FECHAS al espacio de Filtros y se elige la opción Rango de fechas y como se quieren mostrar si la fecha completa o en meses o dias o el formato que se requiera y se le da mostrar filtro.

4. ¿Que es un archivo hyper en tableau, y en que caso de uso se puede aplicar?

Un archivo .hyper en Tableau es una extracción de datos que guarda la información de forma comprimida y optimizada para que el análisis sea mucho más rápido. Básicamente, es una copia de los datos originales que Tableau puede procesar con mayor eficiencia gracias a su motor interno llamado Hyper, este tipo de archivo se usa cuando se quiere mejorar el rendimiento de los dashboards, trabajar sin conexión a la fuente de datos o cuando se necesita resumir y filtrar información antes de analizarla.

Por ejemplo, si tengo una base de datos muy grande en SQL con millones de registros, puedo crear un archivo .hyper con solo la información del último año. Así, Tableau trabaja más rápido y puedo desarrollar mis reportes sin depender de la conexión directa al servidor.
