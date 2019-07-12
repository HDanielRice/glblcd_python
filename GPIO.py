from gpiozero import LED
import time

led = LED(17)

led.on()
time.sleep(5)
led.off()