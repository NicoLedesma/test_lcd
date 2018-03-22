# requires RPi_I2C_driver.py
# -*- coding: utf-8 -*-
import RPi_I2C_LCD
from time import *
import getCharacter

lcd = RPi_I2C_LCD.LCD()
lcd.set_backlight(True)

a = True
# funny face - genero el array con la carita
# let's define a custom icon, consisting of 6 individual characters
# 3 chars in the first row and 3 chars in the second row
font_data_1 = [
    # Char 0 - Upper-left
    [0x00, 0x00, 0x03, 0x04, 0x08, 0x19, 0x11, 0x10],
    # Char 1 - Upper-middle
    [0x00, 0x1F, 0x00, 0x00, 0x00, 0x11, 0x11, 0x00],
    # Char 2 - Upper-right
    [0x00, 0x00, 0x18, 0x04, 0x02, 0x13, 0x11, 0x01],
    # Char 3 - Lower-left
    [0x12, 0x13, 0x1b, 0x09, 0x04, 0x03, 0x00, 0x00],
    # Char 4 - Lower-middle
    [0x00, 0x11, 0x1f, 0x1f, 0x0e, 0x00, 0x1F, 0x00],
    # Char 5 - Lower-right
    [0x09, 0x19, 0x1b, 0x12, 0x04, 0x18, 0x00, 0x00],
    # Char 6 - my test
    [0x1f, 0x0, 0x4, 0xe, 0x0, 0x1f, 0x1f, 0x1f],
]

# Welcome banner
def welcome_banner():
    lcd.clear()
    sleep(1)
    lcd.set_cursor(row=0)
    lcd.message("    Bienvenidos a   ")
    lcd.set_cursor(row=1)
    lcd.message("     PEPECITO'S     ")
    lcd.set_cursor(row=2)
    sleep(1)
    lcd.message("Ingrese contrasenia ")
    lcd.set_cursor(row=3)
    lcd.message("       ------       ")
    sleep(1)
    #lcd.set_backlight(False)


# Testing lines...
lcd.clear()
lcd.set_cursor(row=0)
lcd.message("cargando...")
sleep(1)
lcd.set_cursor(row=1, col=3)
lcd.message("......")
sleep(1)
lcd.set_cursor(row=2, col=5)
lcd.message("......")
sleep(1)
lcd.set_cursor(row=3, col=0)
lcd.message("por favor espere...")
sleep(4)

# Testing on/off back light
lcd.clear()
lcd.set_backlight(False)
lcd.set_cursor(row=0)
lcd.message("...probando backlight...")
lcd.set_cursor(row=1)
lcd.message("prendiendo en 2 seg.")
sleep(2)
lcd.set_backlight(True)

#Sistema KASP
lcd.clear()
sleep(1)
lcd.set_cursor(row=0)
lcd.message("     SISTEMA DE    ")
lcd.set_cursor(row=1)
lcd.message("     ASISTENCIA    ")
sleep(1)
lcd.set_cursor(row=2)
lcd.message("      *******      ")
sleep(1)s
lcd.set_cursor(row=3)
lcd.message("        KASP       ")
sleep(4)


# load logo chars (font_data_1)
lcd.load_custom_chars(font_data_1)
# Write first three chars to row 1 directly
lcd.clear()
lcd.set_cursor(col=8, row=1)
lcd.write_char(0)
lcd.write_char(1)
lcd.write_char(2)
# Write next three chars to row 2 directly
lcd.set_cursor(col=8, row=2)
lcd.write_char(3)
lcd.write_char(4)
lcd.write_char(5)
sleep(4)

welcome_banner()
pw = []
while(a==True):
    #salir = raw_input()
    lcd.set_cursor(col=8, row=3)
    getch = _Getch()
    teclaPulsada=getch.__call__()
    pw.append(teclaPulsada)

    if(teclaPulsada=="*"):
        a=False
        break
    else:
        lcd.message(pw)
        #sleep(2)
        #welcome_banner()


'''

# Now let's define some more custom characters
font_data_2 = [
    # Char 0 - left arrow
    [0x1, 0x3, 0x7, 0xf, 0xf, 0x7, 0x3, 0x1],
    # Char 1 - left one bar
    [0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10],
    # Char 2 - left two bars
    [0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18],
    # Char 3 - left 3 bars
    [0x1c, 0x1c, 0x1c, 0x1c, 0x1c, 0x1c, 0x1c, 0x1c],
    # Char 4 - left 4 bars
    [0x1e, 0x1e, 0x1e, 0x1e, 0x1e, 0x1e, 0x1e, 0x1e],
    # Char 5 - left start
    [0x0, 0x1, 0x3, 0x7, 0xf, 0x1f, 0x1f, 0x1f],
    # Char 6 -
    # [ ],
]
# Load logo chars from the second set
lcd.load_custom_chars(font_data_2)
# display two blocks in columns 5 and 6 (i.e. AFTER col. 4) in row 1
# first draw  two blocks on 5th column (cols 5 and 6), starts from 0
lcd.home()
lcd.message(chr(255)*2)

# draw progress bar
col = 2
lcd.set_cursor(col, 0)
lcd.write_char(1)
sleep(0.2)
lcd.set_cursor(col, 0)getch = _Getch()

    teclaPulsada=getch.__call__()
lcd.write_char(2)
sleep(0.2)
lcd.set_cursor(col, 0)
lcd.write_char(3)
lcd.set_cursor(col, 0)
lcd.write_char(4)
sleep(0.2)
lcd.set_cursor(col, 0)
lcd.write_char(255)
sleep(0.2)
# next column
col += 1
lcd.set_cursor(col, 0)
lcd.write_char(1)
sleep(0.2)
lcd.set_cursor(col, 0)
lcd.write_char(2)
sleep(0.2)getch = _Getch()

    teclaPulsada=getch.__call__()
lcd.set_cursor(col, 0)
lcd.write_char(3)
lcd.set_cursor(col, 0)
lcd.write_char(4)
sleep(0.2)
lcd.set_cursor(col, 0)
lcd.write_char(255)
sleep(0.2)

# load again funny face and display it
lcd.load_custom_chars(font_data_1)
lcd.set_cursor(row=1, col=9)
lcd.write_char(0)
lcd.set_cursor(row=1, col=10)
lcd.write_char(1)getch = _Getch()

    teclaPulsada=getch.__call__()
lcd.set_cursor(row=1, col=11)
lcd.write_char(2)
lcd.set_cursor(row=2, col=9)
lcd.write_char(3)
lcd.set_cursor(row=2, col=10)
lcd.write_char(4)
lcd.set_cursor(row=2, col=11)
lcd.write_char(5)
sleep(2)

lcd.clear()


lcd.set_cursor(col=1, row=1)
lcd.write_msg("HOLA NICO!!!!!")  #Agregue este comando a la libreria!!!

lcd.set_backlight(False)
'''
