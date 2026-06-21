#TAREA: IMPORTAR A PANDAS
import pandas as pd

#TAREA: CREAR UNA FUNCION limpiar_datos_gasto(data_frame_gasto):

#limpiar la descripcion para verificar que sie s un string, que no tienes espacios y que esta en minuscula

#limpiar el id para verificar que si es numero y que es mayor que 0
#limpiar el monto para verificar que si es un numero y que es mayor que 0
#verificar que la fecha si es una fecha
#cada uno define que campos para usted de (id, monto, descripcion y fecha) son obligatorios y eliminar los registros que vengan vacios

def limpiar_datos_gasto(data_frame_datos):

    #1.1 se eliminan los espacios si los hay de los campos de tipo texto
    data_frame_gastos["descripciones"]=data_frame_gastos["descripciones"].astype("string").str.strip().str.lower()
    
       #str.strip() elimina los espacios al inicio y al final del texto
       #str.lower() convierte el texto a minusculas para estandarizarlo

    #1.2 se limpian los valores que no tiene los datos esperados
    valores_esperados_descripciones=["Compra de materiales","Pago de servicios","Inversión en tecnología","Gastos de viaje","Entrenamiento del personal","comida","alquiler","mantenimiento","publicidad","otros"]
    data_frame_gastos["descripciones"]=data_frame_gastos["descripciones"].where(
        data_frame_gastos["descripciones"].isin(valores_esperados_descripciones),
        pd.NA
    )

    #2.1 si es un numero verifico que de verdad sea un numero
    data_frame_gastos["id"]=pd.to_numeric(data_frame_gastos["id"])
    data_frame_gastos["montos"]=pd.to_numeric(data_frame_gastos["montos"])

    #2.2 verifico que los valores numericos esten en el rango que me sirven
    data_frame_gastos["id"]=data_frame_gastos[data_frame_gastos["id"]>0]
    data_frame_gastos["montos"]=data_frame_gastos[data_frame_gastos["montos"]>0]

    #3.1 si es una fecha, verificar que efectivamente sea una fecha
    data_frame_gastos["fechas"]=pd.to_datetime(data_frame_gastos["fechas"])    #Convierte a formato de fecha, si no puede convertirlo lo marca como NaT (Not a Time)

    #CASO ESPECIAL: ELIMINO los registros cuyos datos sean vacios
    columnas_obligatorias=["id","descripciones","montos","fechas"]
    data_frame_gastos=data_frame_gastos.dropna(subset=columnas_obligatorias)

    return data_frame_gastos