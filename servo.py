#Circuit Python capacitive touch
import pulseio
import time
import board
import touchio
from adafruit_motor import servo
pwm = pulseio.PWMOut(board.D13, duty_cycle=2 ** 15, frequency = 50)
my_servo = servo.Servo(pwm)
touch_A1 = touchio.TouchIn(board.A1)  # Not a touch pin on Trinket M0!
touch_A2 = touchio.TouchIn(board.A2)  # Not a touch pin on Trinket M0!
i = 5
j = 5
while True:
    my_servo.angle = i
    if touch_A1.value and i < 180:
        i = i + j
        print("Touched A1!")

    if touch_A2.value and i > 0:
        i = i - j
        print("Touched A2!")
    time.sleep(.01)