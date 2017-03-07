
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, template, request, get, static_file
#from LEDSerial import ledColor

def hex_to_rgb(value):
    """Return (red, green, blue) for the color given as #rrggbb."""
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

@route('/static/<filename>')
def serve_static(filename):
    return static_file(filename, root='static')

@route('/LEDControl')
def LEDControl():
    return template('index')

@route('/LEDControl', method='POST')
def do_LEDControl():
    hold = int(request.forms.get('h'))
    print(hold)
    fade = int(request.forms.get('t'))
    print(fade)
    nbr = int(request.forms.get('n'))
    print(nbr)

    color = [[0 for x in range(3)] for y in range(nbr)]
    for i in range(nbr):
        r = "c"+str(i)
        for j in range(3):
            color[i][j] = hex_to_rgb(int(request.forms.get(r)))[j]
    print(color)

    return template('index')


run(host='0.0.0.0', port=8080)
