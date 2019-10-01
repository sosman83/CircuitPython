import time
import board
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import CursorMode

lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)
PI = DigitalInOut(board.D5)
PI.direction = Direction.INPUT
PI.pull = Pull.UP
lcd.set_cursor_mode(CursorMode.LINE)

interrupt = False
x = 0

while True:
    # print(time.monotonic() % 4)
    # print(PI.value)
    lcd.backlight = True
    lcd.set_cursor_pos(0, 0)
    lcd.print("# of interrupts")
    lcd.set_cursor_pos(0, 10)
    if time.monotonic() % 4 < 1:
     lcd.set_cursor_pos(1, 0)
     lcd.print ("is:  ")
     lcd.print ( str (x))
     lcd.print ("    ")
    if PI.value:
        if interrupt == False:
             interrupt = True
             x = x +1
    if not PI.value:
        interrupt = False