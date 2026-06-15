#Rutina para TRANSFORMAR el DataFrame limpio de usuarios
#
#TRANSFORMAR = a partir de datos YA limpios, obtener informacion util
#Para eso usamos 2 herramientas de pandas:
#   - query()   -> FILTRA filas (se queda solo con las que cumplen una condicion)
#   - groupby() -> AGRUPA filas que comparten un valor y aplica una operacion
#                  a cada grupo (sum = suma, count = conteo, mean = promedio)
#
#IMPORTANTE: estas funciones reciben SIEMPRE el data frame YA limpio
#(es decir, la salida de limpiar_datos_usuario)

import pandas as pd


#1. CUANTOS USUARIOS ADULTOS HAY POR NOMBRE   ->  COUNT
#GRAFICA EN EL MAIN: grafico de BARRAS VERTICALES
#   eje X = nombres   /   eje Y = cantidad_usuarios
#   (compara cantidades entre categorias -> barras)
def usuarios_adultos_por_nombre(data_frame_usuarios):

    #1.1 query: nos quedamos SOLO con los mayores o iguales a 18 anios
    adultos = data_frame_usuarios.query("edad >= 18")

    #1.2 groupby: agrupamos por "nombres" y CONTAMOS cuantos id hay en cada grupo
    resultado = (
        adultos
        .groupby("nombres")["id"]
        .count()
        .reset_index(name="cantidad_usuarios")
        .sort_values("cantidad_usuarios", ascending=False)
    )

    return resultado


#2. PROMEDIO DE EDAD POR CORREO   ->  MEAN
#GRAFICA EN EL MAIN: grafico de BARRAS HORIZONTALES
#   eje Y = correo   /   eje X = edad_promedio
#   (los correos son textos largos -> se ven mejor en horizontal)
def promedio_edad_por_correo(data_frame_usuarios):

    #2.1 query: descartamos edades no validas (nos quedamos con edad > 0)
    edades_validas = data_frame_usuarios.query("edad > 0")

    #2.2 groupby: agrupamos por "correo" y sacamos el PROMEDIO de edad de cada grupo
    resultado = (
        edades_validas
        .groupby("correo")["edad"]
        .mean()
        .reset_index(name="edad_promedio")
        .sort_values("edad_promedio", ascending=False)
    )

    return resultado


#3. SUMA DE EDADES DE LOS USUARIOS JOVENES POR NOMBRE   ->  SUM
#GRAFICA EN EL MAIN: grafico CIRCULAR (pastel / pie)
#   cada porcion = un nombre   /   tamanio = suma_edades
#   (muestra como se reparte el total entre los nombres)
def suma_edades_jovenes_por_nombre(data_frame_usuarios):

    #3.1 query: nos quedamos SOLO con los jovenes (menores de 30 anios)
    jovenes = data_frame_usuarios.query("edad < 30")

    #3.2 groupby: agrupamos por "nombres" y SUMAMOS las edades de cada grupo
    resultado = (
        jovenes
        .groupby("nombres")["edad"]
        .sum()
        .reset_index(name="suma_edades")
        .sort_values("suma_edades", ascending=False)
    )

    return resultado


#4. CUANTOS USUARIOS HAY POR CADA EDAD (en un rango de edad)   ->  COUNT
#GRAFICA EN EL MAIN: grafico de LINEA
#   eje X = edad   /   eje Y = cantidad_usuarios
#   (la edad es un valor ordenado/continuo -> linea muestra la tendencia)
def usuarios_por_edad_en_rango(data_frame_usuarios):

    #4.1 query: nos quedamos con las edades entre 18 y 40 (rango: dos condiciones)
    rango = data_frame_usuarios.query("edad >= 18 and edad <= 40")

    #4.2 groupby: agrupamos por "edad" y CONTAMOS cuantos id hay en cada edad
    resultado = (
        rango
        .groupby("edad")["id"]
        .count()
        .reset_index(name="cantidad_usuarios")
        .sort_values("edad", ascending=True)
    )

    return resultado


#5. RESUMEN COMPLETO POR NOMBRE (varias operaciones a la vez)  ->  COUNT + MEAN + SUM
#GRAFICA EN EL MAIN: grafico de BARRAS AGRUPADAS
#   eje X = nombres   /   por cada nombre varias barras juntas:
#   cantidad_usuarios, edad_promedio y suma_edades
#   (compara las 3 metricas a la vez para cada nombre)
def resumen_por_nombre(data_frame_usuarios):

    #5.1 query: trabajamos solo con usuarios adultos (edad >= 18)
    adultos = data_frame_usuarios.query("edad >= 18")

    #5.2 groupby + agg: agrupamos por "nombres" y aplicamos VARIAS operaciones juntas
    #    - cantidad_usuarios -> count del id
    #    - edad_promedio     -> mean de la edad
    #    - suma_edades        -> sum de la edad
    resultado = (
        adultos
        .groupby("nombres")
        .agg(
            cantidad_usuarios=("id", "count"),
            edad_promedio=("edad", "mean"),
            suma_edades=("edad", "sum")
        )
        .reset_index()
        .sort_values("cantidad_usuarios", ascending=False)
    )

    return resultado
