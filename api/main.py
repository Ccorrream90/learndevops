# coding=utf-8
from flask import Flask, request, render_template
from lib import math_functions

"""
si el archivo math_functions tuviera muuchas funciones y quisiera exportar todas
en vez de poner el nombre, pondría asterisco
por ejemplo con el modulo flask ud solamente esta importando 3 funciones: flask, request, render_template
y si miras bien el codigo, estas utilizando las 4 funciones que importaste
"""

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        vals = request.form.getlist('numberx')
        val1 = float(vals[0])
        val2 = float(vals[1])
        #aqui utilizo la funcion de sumar que manda los dos valores ingresados en el browser
        result = math_functions.addition_fn(val1, val2)
    else:
        val1 = ''
        val2 = ''
        result = ''

    return render_template("form.html",val1=val1, val2=val2, result=result) 
app.run(host= '0.0.0.0')
    
if __name__ == "__main__":
    app.run(host= '0.0.0.0')