#Rutina para simular la fuente de datos que almacena datos de los usuarios
import random
def simular_usuarios(numeroUsuariosASimular):
    #id
    #nombres
    #contraseña
    #edad
    #correo

    #1. PARA SIMULAR DATOS CON PYTHON
    #CREO UNAS SEMILLAS DE LOS DATOS A SIMULAR (TEXTO/NUMERO)
    nombres=["Pedro Perez","Fernanda Fernandez","Rocio Rua","Juan Jimenez","Carlos Cuesta","Maria Martinez","Luisa Lopez","Gaston Galeano","Laura Lopez","Miguel Montoya"]

    contraseñas=["admin123","admin987","user123","user987","person123","person987","gap123","gap987","love123","love987"]

    edades=[20,19,22,24,25,30,29,37,40,65]

    correos=["jl@correo.com","ad@correo.com","lu@correo.com","km@correo.com","ju@correo.com","ad@correo.com","yu@correo.com","hr@correo.com","ew@correo.com","gb@correo.com"]

    #2. CONSTRUIR UN CICLO PARA GENERAR TANTAS SIMULACIONES COMO EL USUARIO FINAL PIDA
    simulaciones_usuario=[]
    for i in range(numeroUsuariosASimular):
        usuario_simulado={
            "id":random.randint(1,500),
            "nombres":random.choice(nombres),
            "contraseña":random.choice(contraseñas),
            "edad":random.choice(edades),
            "correo":random.choice(correos)
        }

        #Inyectar errores controlados en el set de datos
        #(SE HACE PARA QUE LA RUTINA DE SIMULACION SEA LO MAS PARECIDO A LA REALIDAD)
        probabilidadError=random.random()
        if probabilidadError<0.2:
            usuario_simulado["id"]=None
        elif probabilidadError<0.4:
            usuario_simulado["nombres"]=random.choice([None,"11","-10"])
        elif probabilidadError<0.5:
            usuario_simulado["contraseña"]=random.choice([None,"as","-"])
        elif probabilidadError<0.7:
            usuario_simulado["edad"]=random.choice([None,800,-10])
        elif probabilidadError<0.9:
            usuario_simulado["correo"]=" "+usuario_simulado["correo"]+" ".upper()

        simulaciones_usuario.append(usuario_simulado)
    return simulaciones_usuario