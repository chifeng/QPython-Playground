#qpy:2
#qpy:webapp:Hello Qpython
#qpy://localhost:8080/hello
"""
This is a sample for qpython webapp
"""
from bottle import route, run

@route('/hello')
def hello():
    return "Hello World!"

run(host='localhost', port=8080)
