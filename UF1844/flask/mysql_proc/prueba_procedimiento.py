import mysql.connector

conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    port = '3360',
    password = 'password_que_quieras_para_root',
    database = 'jardineria'
)

cursor = conexion.cursor()
cursor.execute('call contar_gama(%s)',('frutales',))

resultado = cursor.fetchall()

for fila in resultado:
    print(fila)

cursor.close()
conexion.close()