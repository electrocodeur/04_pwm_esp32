from machine import Pin, PWM
from time import sleep

# Configuration de la broche 15 en mode PWM
led = PWM(Pin(15), freq=1000)

"""while True:
    led.duty(0)# 0%
    sleep(1)
    led.duty(255)# 25%
    sleep(1)
    led.duty(510)# 50%
    sleep(1)
    led.duty(765)# 75%
    sleep(1)
    led.duty(1023)# 100%
    sleep(1)
"""
# Fonction pour faire varier la luminosité de la LED
def vary_brightness(pwm):
    duty = 0
    direction = 1
    while True:
        pwm.duty(duty)
        duty += direction * 10
        if duty >= 1023:
            duty = 1023
            direction = -1
        elif duty <= 0:
            duty = 0
            direction = 1
        sleep(0.01)

# Appel de la fonction pour faire varier la luminosité
vary_brightness(led)