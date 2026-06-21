#Rutina para generar multiples fuentes de datos de un set simulado

#TAREA construir funcion generar gastos en json,csv

import pandas as pd

def convertir_lista_a_fuentes_gastos(lista_datos):

    data_frame_datos=pd.DataFrame(lista_datos)

    data_frame_datos.to_json(
        "gastos.json",
        orient="records", #registros de datos en formato JSON
        indent=4 #formato legible con indentación
    )

    data_frame_datos.to_csv(
        "gastos.csv",
        index=False #no incluir el índice en el archivo CSV
    )

    '''data_frame_datos.to_excel(
        "gastos.xlsx",
        index=False #no incluir el índice en el archivo Excel
    )'''