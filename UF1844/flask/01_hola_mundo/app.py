from flask import Flask, render_template, request


app = Flask(__name__)
@app.route('/index')
@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/hola')
def hola():
    cadena = """ 
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <h1>Saludos! quien vive?</h1>
            <h2>Sois amigo o enemigo</h2>
        </body>
        </html>
        """
    return cadena

@app.route('/prueba')
def prueba():
    return render_template('prueba.html')


@app.route('/prueba1/')
@app.route('/prueba1/<string:nombre>')
@app.route('/prueba1/<string:nombre>/<int:numero>')

def saludos(nombre=None,numero=None):
    salida = ""
    if nombre and numero:
        salida = f"Hola {nombre} tienes {numero} años, pero has pegado la viejá"
    elif nombre:
        salida = f"Hola {nombre}"
    else:
        salida = f"Qué dice el tío?"

    return salida

@app.route('/suma', methods=['GET','POST'])
def sumar():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        return str(int(num1) + int(num2))
    else:
        cadena='''
        <form action="/suma" method="POST">

            <label>N1:</label>
            <input type="text" name="num1"/>

            <label>N2:</label>
            <input type="text" name="num2"/>

            <input type="submit" value="Suma"/>
        </form>
        '''
        return cadena

if __name__ == '__main__':
    app.run(debug=True)
