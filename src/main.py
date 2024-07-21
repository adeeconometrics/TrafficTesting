from flask import Flask
from random import randint
from time import sleep

app = Flask(__name__)

@app.route('/')
def index() -> str:
    return "OK"

@app.route('/about')
def about() -> str:
    return "About page"

@app.route('/random')
def random() -> str:
    sleep(randint(1,3))
    return "Random page"