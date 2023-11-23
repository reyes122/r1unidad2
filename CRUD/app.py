#Bryan Adrian Reyes Ibarra
#GIR0541
#CRUD videojuegos
#23 de noviembre del 2023


import json
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Establece la conexión con la base de datos
def get_db_connection():
    conn = sqlite3.connect('CRUD.db')
    conn.row_factory = sqlite3.Row
    return conn

# Método GET para obtener todos los registros de la tabla Videojuegos
@app.route('/videojuegos', methods=['GET'])
def get_videojuegos():
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Videojuegos')
    data = cursor.fetchall()
    for reg in data:
        registros.append(dict(reg))
    conn.close()
    return jsonify(registros)

# Método GET para obtener todos los registros de la tabla Desarrolladora
@app.route('/desarrolladoras', methods=['GET'])
def get_desarrolladoras():
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Desarrolladora')
    data = cursor.fetchall()
    for reg in data:
        registros.append(dict(reg))
    conn.close()
    return jsonify(registros)

# Método PUT para crear un registro en la tabla Videojuegos
@app.route('/videojuegos', methods=['PUT'])
def create_videojuego():
    record = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    insert = 'INSERT INTO Videojuegos (IDVideojuego, Nombre, Genero, Lanzamiento, DesarrolladoraID, Plataforma, Precio, Ventas, ModoMultijugador, Descripcion) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    cursor.execute(insert, (record['IDVideojuego'], record['Nombre'], record['Genero'], record['Lanzamiento'], record['DesarrolladoraID'], record['Plataforma'], record['Precio'], record['Ventas'], record['ModoMultijugador'], record['Descripcion']))
    conn.commit()
    return jsonify(record)

# Método PUT para crear un registro en la tabla Desarrolladora
@app.route('/desarrolladoras', methods=['PUT'])
def create_desarrolladora():
    record = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    insert = 'INSERT INTO Desarrolladora (IdDesarrolladora, Nombre, PaisOrigen, Fundacion, Empleados, Website, Contacto, Experiencia) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
    cursor.execute(insert, (record['IdDesarrolladora'], record['Nombre'], record['PaisOrigen'], record['Fundacion'], record['Empleados'], record['Website'], record['Contacto'], record['Experiencia']))
    conn.commit()
    return jsonify(record)

# Método DELETE para eliminar un registro de la tabla Videojuegos
@app.route('/videojuegos', methods=['DELETE'])
def delete_videojuego():
    record = json.loads(request.data)
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM Videojuegos WHERE IDVideojuego = ?'
    cursor.execute(delete, (record['IDVideojuego'],))
    conn.commit()
    return jsonify(record)

# Método DELETE para eliminar un registro de la tabla Desarrolladora
@app.route('/desarrolladoras', methods=['DELETE'])
def delete_desarrolladora():
    record = json.loads(request.data)
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM Desarrolladora WHERE IdDesarrolladora = ?'
    cursor.execute(delete, (record['IdDesarrolladora'],))
    conn.commit()
    return jsonify(record)

# Método POST para actualizar un registro en la tabla Videojuegos
@app.route('/videojuegos', methods=['POST'])
def update_videojuego():
    record = json.loads(request.data)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    update = 'UPDATE Videojuegos SET Nombre = ?, Genero = ?, Lanzamiento = ?, DesarrolladoraID = ?, Plataforma = ?, Precio = ?, Ventas = ?, ModoMultijugador = ?, Descripcion = ? WHERE IDVideojuego = ?'
    cursor.execute(update, (record['Nombre'], record['Genero'], record['Lanzamiento'], record['DesarrolladoraID'], record['Plataforma'], record['Precio'], record['Ventas'], record['ModoMultijugador'], record['Descripcion'], record['IDVideojuego']))
    conn.commit()
    return jsonify(record)

# Método POST para actualizar un registro en la tabla Desarrolladora
@app.route('/desarrolladoras', methods=['POST'])
def update_desarrolladora():
    record = json.loads(request.data)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    update = 'UPDATE Desarrolladora SET Nombre = ?, PaisOrigen = ?, Fundacion = ?, Empleados = ?, Website = ?, Contacto = ?, Experiencia = ? WHERE IdDesarrolladora = ?'
    cursor.execute(update, (record['Nombre'], record['PaisOrigen'], record['Fundacion'], record['Empleados'], record['Website'], record['Contacto'], record['Experiencia'], record['IdDesarrolladora']))
    conn.commit()
    return jsonify(record)

# Inicia el servicio
if __name__ == '__main__':
    app.run(debug=True)
