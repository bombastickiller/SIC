from pathlib import Path    
is_rpi = Path("/etc/rpi-issue").exists()

if not is_rpi:
    from tkgpio import TkCircuit
    #Initialice the circuit inside the GUI
    configuration = {
        "with": 300,
        "height": 200,
        "leds":[
            {"x": 50, "y":40, "name": "LED 1", "pin": 14},
        ],
    }
    circuit = TkCircuit(configuration)
    #circuit.eun
    def main():
        from gpiozero import LED, Button
        from time import sleep
    
        led1 = LED(14)
        led1.blink()
        while True:
            sleep(1)
if is_rpi:
    main()
else:
    circuit.run(main)