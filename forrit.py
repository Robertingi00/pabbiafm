from bottle import *

@route('/')
def index():
    return template('index')

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./img')

run(host="0.0.0.0", port=os.environ.get('PORT'))
