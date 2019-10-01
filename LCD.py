import time
import board
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import CursorMode

lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)
button = DigitalInOut(board.D2)
button.direction = Direction.INPUT
button.pull = Pull.UP
switch = DigitalInOut(board.D5)
switch.direction = Direction.INPUT
switch.pull = Pull.UP
lcd.set_cursor_mode(CursorMode.LINE)

press = False
x = 0

while True:
    print(button.value)
    lcd.backlight = True
    if not button.value:
        if (press == False):
            press = True
            if not switch.value:
                x = x -1
            if switch.value:
                x = x +1
        print((0,))
    if button.value:
        press = False
    lcd.set_cursor_pos(0, 0)
    lcd.print("Presses: ")
    lcd.set_cursor_pos(0, 10)
    lcd.print ( str (x))
    lcd.print ("    ")
    lcd.set_cursor_pos(1, 0)
    lcd.print ("Switch:  ")
    if not switch.value:
        lcd.print ("DOWN")
    if switch.value:
        lcd.print ("UP  ")
    time.sleep(0.05)