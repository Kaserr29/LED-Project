
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import serial
import time

serial = serial.Serial('/dev/ttyACM0', 9600)

#{"d":1000,"h":1000,"n":4,"c":[[255,0,0],[0,255,0],[0,0,255],[255,255,255]]}
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
    cmd += str(c[i])
    cmd += "]}0"

    print(cmd)
