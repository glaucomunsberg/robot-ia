from machine import Pin
from neopixel import NeoPixel
import time

pin = Pin(48, Pin.OUT)   # set GPIO48  to output to drive NeoPixel

color = 1

while True:
    neo = NeoPixel(pin, 1)   # create NeoPixel driver on GPIO48 for 1 pixel
    if color == 1:
        neo[0] = (255, 255, 255)  # set the first pixel to white
        color = 0
    else:
        neo[0] = (255,0,0)  # set the first pixel to white
        color = 1
    neo.write()              # write data to all pixels
    r, g, b = neo[0]         # get first pixel colour
    time.sleep(1)