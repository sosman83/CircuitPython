import board
import time
import neopixel
from adafruit_hcsr04 import HCSR04
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
trig = board.D5
echo = board.D10
sonar = HCSR04 (trig, echo)
while True:
    try:
        n = sonar.distance
        if (n < 15):
            R = abs(5 - n)
            redfloat = (255 - R*25.5)
            red = int(round(redfloat))
        elif (n > 15):
            red = 0
        if (n > 10):
            if (n < 30):
                B = abs(20 - n)
                bluefloat =(255 - B*25.5)
                blue = int(round(bluefloat))
            elif (n > 30):
                blue = 0
        elif (n < 10):
            blue = 0
        if (n > 25):

            G = abs (35 - n)
            greenfloat = (255 - G*25.5)
            green = int(round(greenfloat))
        elif (n < 25):
            green = 0
        print (sonar.distance)
        #print (red, green, blue)
        color = (red, green, blue)
        dot.fill (color)
    except:
        print ("retry")
    time.sleep (0.1)
