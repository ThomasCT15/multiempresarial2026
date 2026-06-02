import pandas as pd

#Codigo principal que ejecutara la ETL (Encargado de ejecutar el analisis de datos)

from notebook.simulaciones.simulacionUsuario import simular_usuarios
from notebook.simulaciones.generacionUsuario import convertir_lista_a_fuentes

#TAREA: importar en esta linea su funcion simuladora de gastos
#TAREA: importar en esta linea su funcion gemeradora de fuentes csv/json de gastos

usuarios=simular_usuarios(1000)
convertir_lista_a_fuentes(usuarios)

#TAREA: Cree la variable gastos=a su funcion
#TAREA: llamar a convertirlistade gastos en fuentes


data_frame_usuarios=pd.DataFrame(usuarios)
#Tarea crear un data frame de gastos

