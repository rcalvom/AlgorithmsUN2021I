
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index1():
    return render_template('HomeAutomation.html')


@app.route('/HomeAutomation')
def index2():
    return render_template('HomeAutomation.html')


@app.route('/SmartCities')
def index3():
    return render_template('SmartCities.html')


@app.route('/SmartFarming')
def index4():
    return render_template('SmartFarming.html')


@app.route('/SmartSupplyChain')
def index5():
    return render_template('SmartSupplyChain.html')