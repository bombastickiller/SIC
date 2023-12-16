from gpiozero import Button,LED
from time import sleep

but = Button(18)
verde = LED(13)
amarillo = LED(19)
rojo = LED(26)
verde.on()
while True:
    if but.is_pressed & verde.value == 1:
        verde.off()
        rojo.off()
        amarillo.on()
        sleep(1)
    elif but.is_pressed & amarillo.value == 1:
        amarillo.off()
        verde.off()
        rojo.on()
        sleep(1)
    elif but.is_pressed & rojo.value == 1:
        rojo.off()
        amarillo.off()
        verde.on()
        sleep(1)