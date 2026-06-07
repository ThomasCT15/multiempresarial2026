#Rutina para TRANSFORMAR el DataFrame limpio de gastos
#
#TRANSFORMAR = a partir de datos YA limpios, obtener informacion util usando:
#   - query()   -> FILTRA filas (se queda solo con las que cumplen una condicion)
#   - groupby() -> AGRUPA filas que comparten un valor y aplica una operacion
#                  a cada grupo (sum = suma, count = conteo, mean = promedio)
#
#RECUERDE: estas funciones reciben SIEMPRE el data frame YA limpio
#(la salida de limpiar_datos_gasto).
#Columnas disponibles del gasto:  id, fecha, monto, descripcion
#
#Mire como quedo resuelto el ejemplo de USUARIOS en transformarUsuario.py
#y resuelva aqui los 5 ejercicios de GASTOS de la misma forma.

import pandas as pd


#EJERCICIO 1: TOTAL GASTADO POR CATEGORIA (descripcion)   ->  SUM
def total_gastado_por_descripcion(data_frame_gastos):
    #TAREA 1.1 query: quedarse solo con los gastos cuyo monto sea mayor a 0
    gastos_validos = data_frame_gastos.query("monto > 0")
    #TAREA 1.2 groupby: agrupar por "descripcion" y SUMAR el monto de cada grupo
    resultado = (
        gastos_validos
        .groupby("descripcion")
        .agg({"monto": "sum"})
        .reset_index(name="monto_total")
        .sort_values("monto_total", ascending=False)
    )
    #TAREA 1.3 ordenar de mayor a menor y retornar el resultado
    return resultado
#reset_index sirve para convertir el resultado del groupby (que tiene la descripcion como indice) en un data frame normal con una columna "descripcion" y otra "monto_total"
#sort_values es la forma de ordenar el resultado por una columna especifica (en este caso monto_total)


#EJERCICIO 2: PROMEDIO DE GASTO POR CATEGORIA (descripcion)   ->  MEAN
def promedio_gasto_por_descripcion(data_frame_gastos):
    #TAREA 2.1 query: quedarse solo con los montos validos (monto > 0)
    gastos_validos = data_frame_gastos.query("monto > 0")
    #TAREA 2.2 groupby: agrupar por "descripcion" y sacar el PROMEDIO (mean) del monto
    resultado = (
        gastos_validos
        .groupby("descripcion")
        .agg({"monto": "mean"})
        .reset_index(name="monto_promedio")
        .sort_values("monto_promedio", ascending=False)
    )
    #TAREA 2.3 ordenar de mayor a menor y retornar el resultado
    return resultado


#EJERCICIO 3: CUANTOS GASTOS HIZO CADA USUARIO (id)   ->  COUNT
def cantidad_gastos_por_usuario(data_frame_gastos):
    #TAREA 3.1 query: quedarse solo con los gastos cuyo monto sea mayor a 0
    gastos_validos = data_frame_gastos.query("monto > 0")
    #TAREA 3.2 groupby: agrupar por "id" y CONTAR cuantos gastos tiene cada usuario
    resultado = (
        gastos_validos
        .groupby("id")
        .count()
        .reset_index(name="cantidad_gastos")
        .sort_values("cantidad_gastos", ascending=False)
    )
    #TAREA 3.3 ordenar de mayor a menor y retornar el resultado
    return resultado


#EJERCICIO 4: GASTOS GRANDES POR CATEGORIA (filtro por monto)   ->  COUNT
def gastos_grandes_por_descripcion(data_frame_gastos):
    #TAREA 4.1 query: quedarse SOLO con los gastos grandes (por ejemplo monto > 100000)
    gastos_grandes = data_frame_gastos.query("monto > 100000")
    #TAREA 4.2 groupby: agrupar por "descripcion" y CONTAR cuantos gastos grandes hay
    resultado = (
        gastos_grandes
        .groupby("descripcion")
        .count()
        .reset_index(name="cantidad_gastos_grandes")
        .sort_values("cantidad_gastos_grandes", ascending=False)
    )
    #TAREA 4.3 ordenar de mayor a menor y retornar el resultado
    return resultado


#EJERCICIO 5: RESUMEN COMPLETO POR CATEGORIA   ->  COUNT + MEAN + SUM
def resumen_por_descripcion(data_frame_gastos):
    #TAREA 5.1 query: quedarse solo con los montos validos (monto > 0)
    gastos_validos = data_frame_gastos.query("monto > 0")
    #TAREA 5.2 groupby + agg: agrupar por "descripcion" y calcular a la vez:
    #          - cantidad_gastos -> count del id
    #          - monto_promedio  -> mean del monto
    #          - monto_total     -> sum del monto
    resultado = (
        gastos_validos
        .groupby("descripcion")
        .agg(
            cantidad_gastos=("id", "count"),
            monto_promedio=("monto", "mean"),
            monto_total=("monto", "sum")
        )
        .reset_index()
        .sort_values("monto_total", ascending=False)
    )
    #TAREA 5.3 ordenar por monto_total de mayor a menor y retornar el resultado
    return resultado

#agg es una forma de aplicar varias operaciones a la vez en un groupby:
#la clave es el nombre de la nueva columna que queremos crear
    