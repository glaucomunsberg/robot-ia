from machine import Pin, PWM
from time import sleep

BUZZER_PIN = 18  # Define o pino do buzzer
buzzer = PWM(Pin(BUZZER_PIN))  # Configura o pino como saída PWM
buzzer.freq(2300)  # Define a frequência do som (1kHz)

while True:
    buzzer.duty(512)  # Ativa o buzzer com metade do ciclo de trabalho (0-1023)
    sleep(1)          # Mantém o som por 1 segundo
    buzzer.duty(0)    # Desliga o som
    sleep(1)          # Espera 1 segundo antes de repetir
    print("next...")