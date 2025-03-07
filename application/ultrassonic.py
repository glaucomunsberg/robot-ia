from machine import Pin, time_pulse_us
import time

# Definição dos pinos
TRIG_PIN = 5
ECHO_PIN = 18

# Velocidade do som em cm/us
SOUND_SPEED = 0.034
CM_TO_INCH = 0.393701

# Configuração dos pinos
trig = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)

def get_distance():
    # Gera um pulso de 10µs no TRIG
    trig.off()
    time.sleep_us(2)
    trig.on()
    time.sleep_us(10)
    trig.off()
    
    # Mede o tempo do pulso no ECHO
    duration = time_pulse_us(echo, 1, 30000)  # Máximo de 30ms para timeout
    
    print("duration: ",duration)
    if duration < 0:
        print("Erro: Sem resposta do sensor")
        return None, None
    
    
    # Calcula a distância em cm e polegadas
    distance_cm = (duration * SOUND_SPEED) / 2
    distance_inch = distance_cm * CM_TO_INCH
    
    return distance_cm, distance_inch

while True:
    distance_cm, distance_inch = get_distance()
    
    if distance_cm is not None:
        print("Distance (cm):", distance_cm)
        print("Distance (inch):", distance_inch)
    
    time.sleep(1)