import os
import pandas as pd

from notebook.descripcion.descripcionUsuario import consumir_api_usuarios
from notebook.descripcion.descripcionGasto import consumir_api_gastos
from notebook.limpieza.limpiezaUsuario import limpiar_datos_usuario
from notebook.limpieza.limpiezaGasto import limpiar_datos_gasto
from notebook.transformacion.transformarUsuario import promedio_edad_por_correo
from notebook.transformacion.transformarUsuario import suma_edades_jovenes_por_nombre
from notebook.transformacion.transformarUsuario import usuarios_por_edad_en_rango
from notebook.transformacion.transformarUsuario import resumen_por_nombre
from notebook.transformacion.transformarUsuario import usuarios_adultos_por_nombre
from notebook.transformacion.transformacionGasto import total_gastado_por_descripcion
from notebook.transformacion.transformacionGasto import promedio_gasto_por_descripcion
from notebook.transformacion.transformacionGasto import cantidad_gastos_por_usuario
from notebook.transformacion.transformacionGasto import gastos_grandes_por_descripcion
from notebook.transformacion.transformacionGasto import resumen_por_descripcion

from notebook.reportes.graficasGenericas import grafica_barras,grafica_linea,grafica_torta,_mostrar_o_guardar


#Rutina de analis de datos de usuarios
#1. Consumo del api para obtener los datos crudos
datos_usuarios=consumir_api_usuarios()

#2. Creando un data frame con los datos del usuario
datos_usuarios_df=pd.DataFrame(datos_usuarios)

#3. Limpiamos los datos
datos_usuarios_limpios=limpiar_datos_usuario(datos_usuarios_df)

#4. Transformar los datos para generar las agrupaciones
adultos=usuarios_adultos_por_nombre(datos_usuarios_limpios)
promedio_correo=promedio_edad_por_correo(datos_usuarios_limpios)
suma_jovenes=suma_edades_jovenes_por_nombre(datos_usuarios_limpios)
usuarios_por_edad=usuarios_por_edad_en_rango(datos_usuarios_limpios)
resumen=resumen_por_nombre(datos_usuarios_limpios)


#5. Con las tarnsformaciones graficamos
#Grafica 1
carpeta_graficas="graficas"
os.makedirs(carpeta_graficas,exist_ok=True)

grafica_barras(adultos["nombres"],adultos["cantidad_usuarios"],"cantidad de usuarios por nombre","nombres","cantidad usuarios",os.path.join(carpeta_graficas,"grafica1.png"))

#Grafica2
grafica_barras(promedio_correo["correo"],promedio_correo["edad_promedio"],"Edad promedio por correo", "Correo","Edad promedio",os.path.join(carpeta_graficas,"grafica2.png"))

#Grafica 3
grafica_torta(suma_jovenes["nombres"],suma_jovenes["suma_edades"],"suma de edades de usuarios jovenes por nombre",os.path.join(carpeta_graficas,"grafica3.png"))

#Grafica 4
grafica_linea(usuarios_por_edad["edad"],usuarios_por_edad["cantidad_usuarios"], "cantidad de usuarios por edad","Edad","Cantidad",os.path.join(carpeta_graficas,"grafica4.png"))

#Grafica 5
grafica_barras(resumen["nombres"],resumen["cantidad_usuarios"],"Resumen por nombre","Nombres","Cantidad",os.path.join(carpeta_graficas,"grafica5.png"))


#Rutina de analisis de datos de gastos
#Tarea: consumir el api de gastos
datos_gastos=consumir_api_gastos()
#tarea: crear df con los datos consumidos del api gastos
datos_gastos_df=pd.DataFrame(datos_gastos)
#tarea: llamar a la funcion que limpia el df de gastos
datos_gastos_limpios=limpiar_datos_gasto(datos_gastos_df)
#tarea: llamar a la funcion que agrupa los datos de gastos
total_gastado=total_gastado_por_descripcion(datos_gastos_limpios)
promedio_gasto=promedio_gasto_por_descripcion(datos_gastos_limpios)
cantidad_gastos=cantidad_gastos_por_usuario(datos_gastos_limpios)
gastos_grandes=gastos_grandes_por_descripcion(datos_gastos_limpios)
resumen=resumen_por_descripcion(datos_gastos_limpios)
#tarea final graficar las agrupaciones 6,7,8,9,10

#grafica 6
grafica_barras(total_gastado["descripcion"],total_gastado["monto_total"],"Total gastado por descripcion","Descripcion","Monto total",os.path.join(carpeta_graficas,"grafica6.png"))

#grafica 7  
grafica_barras(promedio_gasto["descripcion"],promedio_gasto["monto_promedio"],"Promedio de gasto por descripcion","Descripcion","Monto promedio",os.path.join(carpeta_graficas,"grafica7.png"))

#grafica 8
grafica_torta(cantidad_gastos["id"],cantidad_gastos["cantidad_gastos"],"Cantidad de gastos por usuario","ID Usuario","Cantidad de gastos",os.path.join(carpeta_graficas,"grafica8.png"))

#grafica 9
grafica_barras(gastos_grandes["descripcion"],gastos_grandes["cantidad_gastos_grandes"],"Cantidad de gastos grandes por descripcion","Descripcion","Cantidad de gastos grandes",os.path.join(carpeta_graficas,"grafica9.png"))

#grafica 10
grafica_barras(resumen["descripcion"],resumen["cantidad_gastos"],"Cantidad de gastos por descripcion","Descripcion","Cantidad de gastos",os.path.join(carpeta_graficas,"grafica10.png"))



