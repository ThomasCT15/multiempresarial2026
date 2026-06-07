#Rutina de GRAFICAS GENERICAS
#
#Aqui creamos funciones reutilizables para dibujar graficas con matplotlib.
#Son GENERICAS: no saben de usuarios ni de gastos. Solo reciben datos
#(unas etiquetas y unos valores) y dibujan la grafica.
#
#Asi los estudiantes pueden usarlas en main.py con CUALQUIER resultado de
#sus transformaciones (por ejemplo la salida de groupby).
#
#Se usan 3 tipos de grafica:
#   - LINEA  -> para ver una evolucion o tendencia
#   - BARRAS -> para comparar categorias entre si
#   - TORTA  -> para ver la proporcion (el % de cada parte sobre el total)

import matplotlib.pyplot as plt


#1. GRAFICA DE LINEA
def grafica_linea(etiquetas_x, valores_y, titulo="Grafica de linea",
                  nombre_x="Eje X", nombre_y="Eje Y"):
    #etiquetas_x -> lo que va en el eje horizontal (ej: fechas, edades, nombres)
    #valores_y   -> los numeros que se dibujan (ej: montos, cantidades)

    plt.figure(figsize=(10, 5))                         #tamanio de la ventana
    plt.plot(etiquetas_x, valores_y,                    #dibuja la linea
             marker="o", color="purple")                #punto en cada dato y color
    plt.title(titulo)                                   #titulo de la grafica
    plt.xlabel(nombre_x)                                #nombre del eje X
    plt.ylabel(nombre_y)                                #nombre del eje Y
    plt.grid(True, linestyle="--", alpha=0.5)           #rejilla de fondo
    plt.xticks(rotation=45)                             #gira las etiquetas para que no se peguen
    plt.tight_layout()                                  #acomoda todo para que no se corte
    plt.show()                                          #muestra la grafica en pantalla


#2. GRAFICA DE BARRAS
def grafica_barras(categorias, valores, titulo="Grafica de barras",
                   nombre_x="Categorias", nombre_y="Valores"):
    #categorias -> los grupos a comparar (ej: nombres, descripciones)
    #valores    -> la altura de cada barra (ej: cantidad, suma, promedio)

    plt.figure(figsize=(10, 5))
    plt.bar(categorias, valores, color="mediumpurple")  #dibuja las barras
    plt.title(titulo)
    plt.xlabel(nombre_x)
    plt.ylabel(nombre_y)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


#3. GRAFICA DE TORTA (pastel)
def grafica_torta(etiquetas, valores, titulo="Grafica de torta"):
    #etiquetas -> el nombre de cada porcion (ej: nombres, categorias)
    #valores   -> el tamanio de cada porcion (ej: cantidad, total)

    plt.figure(figsize=(7, 7))
    plt.pie(valores,
            labels=etiquetas,
            autopct="%1.1f%%",                          #muestra el porcentaje de cada porcion
            startangle=90)                              #angulo inicial
    plt.title(titulo)
    plt.axis("equal")                                   #para que la torta salga redonda
    plt.tight_layout()
    plt.show()


#==============================================================================
#EJEMPLO DE COMO USARLAS EN main.py (los muchachos lo hacen en clase):
#
#   from notebook.transformacion.transformarUsuario import usuarios_adultos_por_nombre
#   from notebook.reportes.graficasGenericas import grafica_barras, grafica_torta, grafica_linea
#
#   #resultado es un DataFrame con columnas "nombres" y "cantidad_usuarios"
#   resultado = usuarios_adultos_por_nombre(data_frame_usuarios)
#
#   #BARRAS: comparar cuantos usuarios hay por nombre
#   grafica_barras(resultado["nombres"], resultado["cantidad_usuarios"],
#                  titulo="Usuarios por nombre", nombre_x="Nombre", nombre_y="Cantidad")
#
#   #TORTA: ver la proporcion de cada nombre
#   grafica_torta(resultado["nombres"], resultado["cantidad_usuarios"],
#                 titulo="Proporcion de usuarios por nombre")
#
#   #LINEA: ver una tendencia (ej: cantidad por edad)
#   grafica_linea(resultado["nombres"], resultado["cantidad_usuarios"],
#                 titulo="Tendencia", nombre_x="Nombre", nombre_y="Cantidad")
#==============================================================================
