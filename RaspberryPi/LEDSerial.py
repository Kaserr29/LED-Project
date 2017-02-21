
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import serial
import time

serial = serial.Serial('/dev/ttyACM0', 9600)

def ledColor(r,g,b):
    print(bin(r).format('08b')+bin(g).format('08b')+bin(b).format('08b'))
    serial.write(bin(r).format('08b')+bin(g).format('08b')+bin(b).format('08b'))
