import matplotlib.pyplot as plt

temp = {
	"x":[],
	"y":[]	
}
hume = {
    "x": [],
    "y": []
    }
f = open ("datostemperatura.log","r")
datos = f.readlines()
for lines in datos:
    dato = lines.replace('\n', '').split(',')
    temp["x"].append(dato[0])
    temp["y"].append(dato[1])
    hume["x"].append(dato[0])
    hume["y"].append(dato[1])
for i in range (1,10):
    temp["x"].apend(i)
    temp["y"].apend(i)
    hume["x"].apend(i)
    hume["y"].apend(i)
plt.plot(tmp["x"], temp["y"], color = "r")
plt.show()