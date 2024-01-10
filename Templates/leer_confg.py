velocidadDeParpadeo = 1
def leerConfiguracion():
    global velocidadDeParpadeo
    f = open('conf.ini','r')
    lineas = f.readlines()

    for linea in lineas:
        datos = linea.split('=')
        if (datos[0] == "velocidad"):
            velocidadDeParpadeo = int(datos[1])
    f.close()
    
def grabarConfiguracion():
    global velocidadDeParpadeo
    f = open('conf.ini','w')
    f.write("velocidad="+str(velocidadDeParpadeo)+"/r")
    f.close()
    
leerConfiguracion()

print(f"Velocidad: {velocidadDeParpadeo}")