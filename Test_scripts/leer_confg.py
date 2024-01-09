velocidadDeParpadeo = 1
f = open("conf.ini","r")
lineas = f.readlines()

for linea in lineas:
    datos = linea.split()
    if (datos[0] == "velocidad"):
        velocidadDeParpadeo = int(datos[1])
f.close()

#print(f"Velocidad: {velocidadDeParpadeo}")