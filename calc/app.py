from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)
@app.route('/add')
def add_func():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = add(a, b)

    return str(result)

@app.route('/sub')
def add_func():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = sub(a, b)

    return str(result)

@app.route('/mult')
def add_func():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = mult(a, b)

    return str(result)

@app.route('/div')
def add_func():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = div(a, b)

    return str(result)

operations = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<operator>')
def do_operation(operator):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations[operator](a, b)
    return str(result)
