from machine import Pin, time_pulse_us
import time


PINO_TRIG = 27
PINO_ECHO = 26
PINO_LED_ITENS = 18  #BRANCO
PINO_LED_CAIXAS = 15 #VERDE

trig = Pin(PINO_TRIG, Pin.OUT)
echo = Pin(PINO_ECHO, Pin.IN)
led = Pin(PINO_LED_ITENS, Pin.OUT)
led_caixa = Pin(PINO_LED_CAIXAS, Pin.OUT)


cont_itens = 0
cont_caixas = 0
dist_maxima = 10  
detc = False  


def calc_distancia():
    trig.value(0)
    time.sleep_us(2)

    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    duracao = time_pulse_us(echo, 1, 300000)
    if duracao < 0:  
        return 1000  
    distancia = (duracao / 2) * 0.0343
    return distancia

while True:
    dist = calc_distancia()

    if dist <= dist_maxima:
        led.value(1)  

        if not detc:
            cont_itens += 1
            detc = True
            print("Item detectado! Quantidade:", cont_itens)

           
            if cont_itens >= 10:
                cont_caixas += 1
                cont_itens = 0 
                print("Caixa completa! Número de caixas:", cont_caixas)
                led_caixa.value(1)
                print("Iniciando Próxima Caixa!")

        time.sleep(1)
                

    else:
        led.value(0)
        led_caixa.value(0)

        detc = False

    time.sleep(0.5)
