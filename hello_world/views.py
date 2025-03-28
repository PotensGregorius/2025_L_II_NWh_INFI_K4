from hello_world import app
from hello_world.formater import get_formatted
from hello_world.formater import SUPPORTED, PLAIN
from flask import request

moje_imie = "Grzegorz"
msg = "Hello World!"
JSON = "json"


@app.route('/')
def index():
    output = request.args.get('output')
    if not output:
        output = PLAIN
    return get_formatted(msg, moje_imie, format=JSON)


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)
