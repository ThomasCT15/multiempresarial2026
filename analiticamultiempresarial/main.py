import os
import pandas as pd

from notebook.descripcion.descripcionUsuario import consumir_api_usuarios

from notebook.limpieza.limpiezaUsuario import limpiar_datos_usuario

from notebook.transformacion.transformarUsuario import promedio_edad_por_correo
from notebook.transformacion.transformarUsuario import suma_edades_jovenes_por_nombre
from notebook.transformacion.transformarUsuario import usuarios_por_edad_en_rango
from notebook.transformacion.transformarUsuario import resumen_por_nombre
from notebook.transformacion.transformarUsuario import usuarios_adultos_por_nombre

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
grafica_barras(adultos["nombres"],adultos["cantidad_usuarios"],"cantidad de usuarios por nombre","nombres","cantidad usuarios",os.path.join(carpeta_graficas,"garfica1.png"))



#Rutina de analisis de datos de gastos
#Tarea: consumir el api de gastos
#tarea: crear df con los datos consumidos del api gastos
#tarea: llamar a la funcion que limpia el df de gastos
#tarea: llamar a la funcion que agrupa los datos de gastos



