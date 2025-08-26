from machine import Pin, time_pulse_us
import time

PINO_TRIG = 32
PINO_ECHO = 26

LED_INTRUDER = 27

trig = Pin(PINO_TRIG, Pin.OUT)
echo = Pin(PINO_ECHO, Pin.IN)
led = Pin(LED_INTRUDER, Pin.OUT)

# Fun de calcular distância #
def CalDistancia():
    trig(0)
    time.sleep_us(2)

    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    duracao = time_pulse_us(echo, 1 , 30000)
    distancia = (duracao / 2) * 0.0343
    return distancia


# LOOP #
while True:
    distan = CalDistancia()
    print("Distância:", distan, "cm")

    if distan <= 10:
        print ("Movimento Detectado!!")
        led.value(1)
        time.sleep(1)
    else:
        print("Nenhum movimento Detectado")
        led.value(0)
    time.sleep(3)
     