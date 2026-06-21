#Rutina para simular la fuente de datos que almacena datos de los gastos
#id
#fecha "2026-05-06"
#monto
#descripcion

#TAREA: PROGRAME AQUI FUNCION GENERADORA DE GASTOS SIMULADOS

#TAREA: PROGRAMAR RUTINA PARA INYECTAR ERRORES CONTROLADOS EN LSO CAMPOS ID,FECHA,MONTO,DESCRIPCION

import random

def simular_gastos(numeroGastosASimular):

    #1. PARA SIMULAR DATOS CON PYTHON
    #CFREO UNAS SEMILLAS DE LOS DATOS A SIMULAR (TEXTO/NUMERO)
    fechas =["2026-05-01","2026-05-02","2026-05-03","2026-05-04","2026-05-05","2026-05-06","2026-05-07","2026-05-08","2026-05-09","2026-05-10"]

    montos =[100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000]

    descripciones = ["Compra de materiales","Pago de servicios","Inversión en tecnología","Gastos de viaje","Entrenamiento del personal","comida","alquiler","mantenimiento","publicidad","otros"]

    #2. CONSTRUIR UN CICLO PARA GENERAR TANTAS SIMULACIONES COMO EL USUARIO FINAL PIDA
    simulaciones_gasto=[]
    for i in range(numeroGastosASimular):
        gasto_simulado={
            "id":random.randint(1,500),
            "fecha":random.choice(fechas),
            "monto":random.choice(montos),
            "descripcion":random.choice(descripciones)
        }

        #Inyectar errorres controlados en el set de datos
        #(SE HACE PARA  QUE LA RUTINA DE SIMULACION SEA LO MAS PARECIDO CON LA REALIDAD)
        probabilidadError= random.random() #Genera un numero aleatorio entre 0 y 1
        if probabilidadError < 0.2: #20% de probabilidad de error
            gasto_simulado["id"]=None #Inyectar un ID invalido
        elif probabilidadError < 0.4: #40% de probabilidad de error
            gasto_simulado["fecha"]=None #Inyectar una fecha invalida
        elif probabilidadError < 0.6: #60% de probabilidad de error
            gasto_simulado["monto"]= random.choice([None, -100000]) #Inyectar un monto invalido
        elif probabilidadError < 0.8: #80% de probabilidad de error
            gasto_simulado["descripcion"]=random.choice([None,"11","-10","a"]) #Inyectar una descripción invalida

        simulaciones_gasto.append(gasto_simulado)
    return simulaciones_gasto

