from gpiozero import LED, DistanceSensor
import time

sensor = DistanceSensor(echo = 14, trigger = 15)
led = LED(18)
while True:
	distance = sensor.distance * 100
	print ("Distancia: ", distance)

	if distance < 20:
		led.on()
	else:
		led.off

	time.sleep(0.5)
