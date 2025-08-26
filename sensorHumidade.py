from machine import Pin, ADC
import time

SENSOR_UMIDADE = 26
LED_SECO = 14

sensor_umidade = ADC(Pin(SENSOR_UMIDADE))
led = Pin(LED_SECO, Pin.OUT)

sensor_umidade.width(ADC.WIDTH_12BIT)
sensor_umidade.atten(ADC.ATTN_11DB)

while True:
    valor_umidade = sensor_umidade.read()
    print("Valor do sensor:", valor_umidade)
    
    SOLO_SECO = 2000
    
    if valor_umidade > SOLO_SECO:
        print("ALERTA: Solo seco! Regue a planta!")
        led.value(1)
    else:
        print("Solo úmido. Tudo OK!")
        led.value(0)
        
    time.sleep(5)
    
