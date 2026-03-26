# 1.  Crea una función python que valide una contraseña: 
# La contraseña debe cumplir: 
# ●  Mínimo 8 caracteres 
# ●  Al menos una mayúscula 
# ●  Al menos un número 
# ●  Al menos un carácter especial 
# Devuelve: 
# ●  "Válida" 
# ●  o el motivo del error 

def validar_contraseña(contraseña):

    if len(contraseña) < 8:
        return "La contraseña debe tener al menos 8 caracteres"
    if not any(c.isupper() for c in contraseña):
        return "La contraseña debe contener al menos una mayúscula"
    if not any(c.isdigit() for c in contraseña):
        return "La contraseña debe contener al menos un número"
    if not any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for c in contraseña):
        return "La contraseña debe contener al menos un carácter especial"
    
    return "Válida"

# 2.  Utilizando la base de datos de jardinería, realiza las siguientes consultas: 

# a.  Devuelve un listado de todos los pedidos que fueron rechazados en 2009. 

# SELECT * from pedido p where p.estado = 'rechazado' AND p.fecha_pedido BETWEEN '2009/01/01' and '2009/12/31'

# b.  Devuelve un listado de todos los pedidos que han sido entregados en el mes de enero de cualquier año. 

# SELECT * from pedido p where p.estado = 'entregado' AND MONTH(p.fecha_pedido) = 1

# c.  Devuelve un listado con todos los productos que pertenecen a la gama ornamentales y que tienen más de 100 unidades en stock. El listado deberá estar ordenado por su precio de venta, mostrando en primer lugar los de mayor precio. 

# SELECT * from producto p where p.gama = 'Ornamentales' AND p.stock > 100 ORDER BY p.precio_venta DESC

# d.  Devuelve un listado de las diferentes gamas de producto que ha comprado cada 
# cliente. 

# SELECT  distinct c.nombre_cliente ,p2.gama from cliente c join pedido p on c.codigo_cliente = p.codigo_cliente join detalle_pedido dp on p.codigo_pedido = dp.codigo_pedido join producto p2 on dp.codigo_producto = p2.codigo_producto

# 3.  Dado este JSON: 
# [ 
#  {"nombre": "Ana", "edad": 25}, 
#  {"nombre": "Luis", "edad": 17}, 
#  {"nombre": "Carlos", "edad": 30} 
# ] 

#    Crea un programa python que: 

# 1. Filtre solo los mayores de edad
mayores_edad = [persona for persona in data if persona["edad"] >= 18]

# 2. Muestre sus nombres
nombres = [persona["nombre"] for persona in data]
print("Nombres de personas mayores de edad:", nombres)

# 3. Calcule la edad media
edades = [persona["edad"] for persona in data]
edad_media = sum(edades) / len(edades)
print("Edad media de personas mayores de edad:", edad_media)