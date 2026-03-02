from flask import Flask, render_template, request, redirect, url_for
import utilidades as util

app = Flask(__name__)

PRODUCTOS = 'productos.json'


@app.route('/')
def index():
    id_producto = None
    producto_sel = None
    datos = util.cargar_productos(PRODUCTOS)
    categ = datos["categoria"]
    prods = datos["productos"]

    
    id_producto = request.args.get("producto")
    if id_producto:
        id_producto = int(id_producto)
        for p in prods:
            if p['id'] == id_producto:
                producto_sel = p
                break


    return render_template('index.html', 
                            productos=prods, 
                            categorias=categ,
                            producto=producto_sel)

@app.route('/actualizar/<int:prod_id>', methods=['POST'])
def actualizar_producto(prod_id):

    datos = util.cargar_productos(PRODUCTOS)
    prods = datos["productos"]
    producto_sel = None

    for p in prods:
        if p['id'] == prod_id:
            producto_sel = p
            break

    producto_sel['nombre'] = request.form['nombre']
    producto_sel['precio'] = float(request.form['precio'])
    producto_sel['id_categoria'] = int(request.form['categoria'])

    util.guardar_datos(PRODUCTOS, datos)

    return redirect(url_for('index'))


@app.route('/crear', methods=['POST'])
def crear_producto():
    datos = util.cargar_productos(PRODUCTOS)
    prods = datos['productos']

    producto_nuevo = {
        'id': util.nuevo_id(PRODUCTOS),
        'nombre': request.form.get('nombre', ''),
        'precio': float(request.form.get('precio') or 0),
        'id_categoria': int(request.form.get('categoria') or 0)
    }

    prods.append(producto_nuevo)
    util.guardar_datos(PRODUCTOS, datos)
    return redirect(url_for('index', producto=producto_nuevo['id']))

@app.route('/borrar/<int:prod_id>', methods=['POST'])
def borrar_producto(prod_id):
    datos = util.cargar_productos(PRODUCTOS)
    prods = datos['productos']

    datos['productos'] = [p for p in prods if p['id'] != prod_id]
    util.guardar_datos(PRODUCTOS, datos)
    return redirect(url_for('index'))
