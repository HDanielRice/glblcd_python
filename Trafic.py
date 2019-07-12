from gpiozero import LED, Button
import time
from signal import pause

def traffic(): 
    red = LED(17)
    yellow = LED(24)
    green = LED(25)
    
    red.on()
    waiting_time = time.sleep(10)
    
    while waiting_time != time.sleep(10):
        red.on()
    red.off()
    
    yellow.on()
    time.sleep(5)
    yellow.off()
    green.on()
    time.sleep(10)
    green.off()
    
    def traffic_control():
        button = Button(2)
        button.when_pressed = traffic
        pause()
