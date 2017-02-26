
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
    r = int(request.forms.get('R'))
    print(r)
    g = int(request.forms.get('G'))
    print(g)
    b = int(request.forms.get('B'))
    print(b)
    ledColor(r,g,b)
    return template('index')


run(host='0.0.0.0', port=8080)
