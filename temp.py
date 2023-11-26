import datetime
from random import randrange
from time import sleep
import Adafruit_DHT as AD
sensor = AD.DHT11
pin = 25

while True:
    f = open("datosTemperatura.log","a")
    fecha = datetime.datetime.now()
    #temperatura = randrange (45)
    #humedad = randrange(100)
    humedad, temperatura = AD
    
    dato = f"{fecha},{temperatura},{humedad}"
    print(dato)
    f.write(dato)
    f.close()
    sleep(1.1)