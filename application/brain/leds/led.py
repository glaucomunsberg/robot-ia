from machine import Pin
from neopixel import NeoPixel
import time


class ColorSet:
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    PINK = (255, 192, 203)
    ORANGE = (255, 165, 0)
    PURPLE = (128, 0, 128)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    LIME = (0, 255, 0)
    BLACK = (0, 0, 0)

    def get_color(self, color: str):
        if color == 'RED':
            return self.RED
        elif color == 'GREEN':
            return self.GREEN
        elif color == 'BLUE':
            return self.BLUE
        elif color == 'WHITE':
            return self.WHITE
        elif color == 'YELLOW':
            return self.YELLOW
        elif color == 'PINK':
            return self.PINK
        elif color == 'ORANGE':
            return self.ORANGE
        elif color == 'PURPLE':
            return self.PURPLE
        elif color == 'CYAN':
            return self.CYAN
        elif color == 'OFF':
            return self.BLACK
        else:
            return self.WHITE


class LedESP32:
    color_set = ColorSet()
    pin = None
    color = None

    def __init__(self, pin_number: int = 48, color=None):
        self.pin = Pin(pin_number, Pin.OUT)
        if color is not None:
            self.color = self.color_set.get_color(color)

    def set_color(self, color):
        neo = NeoPixel(self.pin, 1)
        self.color = self.color_set.get_color(color)
        neo[0] = self.color_set.get_color(self.color)
        neo.write()


pin = Pin(48, Pin.OUT)   # set GPIO48  to output to drive NeoPixel

color = 1

while True:
    neo = NeoPixel(pin, 1)   # create NeoPixel driver on GPIO48 for 1 pixel
    if color == 1:
        neo[0] = (255, 255, 255)  # set the first pixel to white
        color = 0
    else:
        neo[0] = (199, 21, 133)  # set the first pixel to white
        color = 1
    neo.write()              # write data to all pixels
    r, g, b = neo[0]         # get first pixel colour
    time.sleep(1)
