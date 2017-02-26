
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import serial
import time

serial = serial.Serial('/dev/ttyACM0', 9600)

def sendJson(d,h,n,c):
