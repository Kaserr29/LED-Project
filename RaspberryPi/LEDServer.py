
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, template, request, get, static_file
#from LEDSerial import ledColor


@get("static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="views/static/css")

@get("static/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="views/static/js")

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

    color[[0 for x in range(3)] for y in range(n)]
    for i in range(n)
        r = "c"+i
        for j in range(3)
            color[i][j] = int(request.forms.get(r))
    print(color)

    return template('index')


run(host='0.0.0.0', port=8080)
