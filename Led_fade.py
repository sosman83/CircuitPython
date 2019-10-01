#Led pulses
#Got this code from Olivia
import board
import pulseio
led = pulseio.PWMOut(board.D13)
import time

while True:
    for i in range (100):
        led.duty_cycle = int(i / 100 * 65535) #makes led get lighter
        time.sleep(0.03) #time when led is fully on
    for i in range (100, -1, -1):
        led.duty_cycle = int(i / 100 * 65535) #makes led get darker
        time.sleep(0.03) #time when led is fully off