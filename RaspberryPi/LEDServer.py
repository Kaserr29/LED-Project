
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, template,request
from LEDSerial import ledColor


@get("static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css"))

@get("static/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="views/static/js"))

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
    return template('index')


run(host='0.0.0.0', port=8080)
