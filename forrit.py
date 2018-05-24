from bottle import *

@route('/')
def index():
    return template('index')

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./img')


run(host='localhost', port='8080', debug='True', reloader='True')