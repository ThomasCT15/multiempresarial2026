#Limpiamos datos para garantizar que nuestro analisis sea de calidad
#No analizamos datos que no tienen proposito

#PASOS GENERICOS PARA LIMPIAR DATOS

#1. LIMPIAR LOS TEXTOS


#2. LIMPIAR LOS NUMEROS


#3. LIMPIAR LAS FECHAS Y OTROS FORMATOS

import pandas as pd

def limpiar_datos_usuario(data_frame_usuarios):

    #1.1 Se eliminan los espacios si los hay de los campos de tipo texto
    data_frame_usuarios["nombres"]=data_frame_usuarios["nombres"].astype("string").str.strip().str.lower()
    data_frame_usuarios["contraseña"]=data_frame_usuarios["contraseña"].astype("string").str.strip().str.lower()
    data_frame_usuarios["correo"]=data_frame_usuarios["correo"].astype("string").str.strip().str.lower()

    #1.2 Se limpian los datos que no tienen valores esperados
    valores_esperados_nombres=["Pedro Perez","Fernanda Fernandez","Rocio Rua","Juan Jimenez","Carlos Cuesta","Maria Martinez","Luisa Lopez","Gaston Galeano","Laura Lopez","Miguel Montoya"]
    data_frame_usuarios["nombres"]=data_frame_usuarios["nombres"].where(
        data_frame_usuarios["nombres"].isin(valores_esperados_nombres),
        pd.NA
    )

    valores_esperados_contraseña=["admin123","admin987","user123","user987","person123","person987","gap123","gap987","love123","love987"]
    data_frame_usuarios["contraseña"]=data_frame_usuarios["contraseña"].where(
        data_frame_usuarios["contraseña"].isin(valores_esperados_contraseña),
        pd.NA
    )

    valores_esperados_correo=["jl@correo.com","ad@correo.com","lu@correo.com","km@correo.com","ju@correo.com","ad@correo.com","yu@correo.com","hr@correo.com","ew@correo.com","gb@correo.com"]
    data_frame_usuarios["correo"]=data_frame_usuarios["correo"].where(
        data_frame_usuarios["correo"].isin(valores_esperados_correo),
        pd.NA
    )


    #2.1 si es un numero verifico que de verdad sea un numero
    data_frame_usuarios["id"]=pd.to_numeric(data_frame_usuarios["id"])
    data_frame_usuarios["edad"]=pd.to_numeric(data_frame_usuarios["edad"])

    #2.2 verifico que los valores numericos esten en el rango que me sirven
    data_frame_usuarios=data_frame_usuarios[data_frame_usuarios["id"]>0]
    data_frame_usuarios=data_frame_usuarios[data_frame_usuarios["edad"]<150]
    data_frame_usuarios=data_frame_usuarios[data_frame_usuarios["edad"]>0]

    #3.1 Si es una fecha, verificar que efectivamnte sea una fecha
    #data_frame_usuarios["fecha"]=pd.to_datetime(data_frame_usuarios["fecha"])

    #CASO especial : ELIMINO los registros cuyos datos sean vacios
    columnas_obligatorias=["id","correo","contraseña"]
    data_frame_usuarios=data_frame_usuarios.dropna(subset=columnas_obligatorias)


    return data_frame_usuarios