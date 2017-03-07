
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import serial
import time

serial = serial.Serial('/dev/ttyACM0', 9600)

def sendJson(d,h,n,c):
    cmd = "{\"d\":"
    cmd += str(d)

    cmd += ", \"h\":"
    cmd += str(h)

    cmd += ", \"n\":"
    cmd += str(n)

    cmd += ", \"c\":["
    for i in range(n-1):
        cmd += str(c[i])
        cmd += ", "
    cmd += str(c[n-1])
    cmd += "]}"

    print(cmd)
    serial.write(cmd)
