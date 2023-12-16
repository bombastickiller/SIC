from gpiozero import LED
import time

led = LED(18)

while True:
	orden = input ("\n\n Que quieres que haga?\n1)enciende\n2)apaga\n3)parpadea \n9)salir \n\n>>\t")
	if (orden == "1"):
		print("prendido")
		led.on()
	if (orden == "3"):
                print("parpadeando")
                led.blink()
	elif (orden == "2"):
		print("apagado....")
		led.off()
	elif (orden == "9"):
		print("saliendo...")
		led.off()
		time.sleep(3)
		break;
	else:
		print("orden invalida")
