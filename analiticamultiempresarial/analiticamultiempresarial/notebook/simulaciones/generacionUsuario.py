#Rutina para generar multiples fuentes de datos de un set simulado

import pandas as pd

def convertir_lista_a_fuentes(lista_datos):

    data_frame_datos=pd.DataFrame(lista_datos)

    data_frame_datos.to_json(
        "usuarios.json",
        orient="records",
        indent=4
    )

    data_frame_datos.to_csv(
        "usuarios.csv",
        index=False
    )

    '''data_frame_datos.to_excel(
        "usuarios.xlsx",
        index=False
    )'''