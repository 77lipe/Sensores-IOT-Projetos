from machine import Pin, time_pulse_us
import time


PINO_ECHO = 25
LED = 14


echo = Pin(PINO_ECHO, Pin.IN)
led = Pin(LED, Pin.OUT)

contador = 0
cont_anterior = 0

# LOOP #
while True:
    cont_atual = echo.value()

    #loopin de contagem
    if cont_atual == 1 and cont_anterior == 0:
        contador +=1
        print("Objeto Detectado!", contador)
        led.value(1)
        time.sleep(2)
        led.value(0)
    cont_anterior = cont_atual
    time.sleep(3)
    elif  cont_atual > 10:
        contador = 0
        print("Caixa completa! Nova caixa")
        time.sleep(5)
       
     