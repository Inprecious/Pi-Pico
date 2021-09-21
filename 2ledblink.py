import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)
led = machine.Pin(0, machine.Pin.OUT)

led.value(1)
led_onboard.value(1)


for i in range(10):
    led_onboard.toggle()
    led.toggle()
    utime.sleep(0.1)
 
 
led.value(0)
led_onboard.value(0)


