# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT
"""CircuitPython Blink Example - the CircuitPython 'Hello, World!'"""
import time
import board
import digitalio
import random

led = [digitalio.DigitalInOut(board.IO15),digitalio.DigitalInOut(board.IO5),digitalio.DigitalInOut(board.IO7),digitalio.DigitalInOut(board.IO9)]
led[0].direction = digitalio.Direction.OUTPUT
led[1].direction = digitalio.Direction.OUTPUT
led[2].direction = digitalio.Direction.OUTPUT
led[3].direction = digitalio.Direction.OUTPUT


random.seed(int(time.monotonic()))
init = [time.monotonic(),time.monotonic(),time.monotonic(),time.monotonic()]
intfin = [random.randint(5,15),random.randint(5,15),random.randint(5,15),random.randint(5,15)]
intext = [random.randint(5,15),random.randint(5,15),random.randint(5,15),random.randint(5,15)]
fin = [intfin[0] / 10,intfin[1] / 10,intfin[2] / 10,intfin[3] / 10]
ext = [intext[0] / 10,intext[1] / 10,intext[2] / 10,intext[3] / 10]
while True:
    #time.sleep(random.randint(1,3))
    now = [time.monotonic(),time.monotonic(),time.monotonic(),time.monotonic()]
    for i in range(0,3):
        if  (now[i] - init[i]) > 0 and (now[i] - init[i]) < fin[i]:
            led[i].value = True
        if  (now[i] - init[i]) > fin[i] and (now[i] - init[i]) < (fin[i]+ext[i]):
            led[i].value = False
        if  (now[i] - init[i]) > fin[i]+ext[i]:
            init[i] = now[i]
            intfin[i] = random.randint(3,12)
            intext[i] = random.randint(3,12)
            fin[i] = intfin[i] / 10
            ext[i] = intext[i] / 10
