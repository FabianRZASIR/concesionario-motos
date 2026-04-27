from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# CONFIGURACIÓN DE CONEXIÓN (IP de tu VM1: 192.168.1.149)
db_config = {
    'host': '192.168.1.149', 
    'user': 'moto_web_user',
    'password': 'WebUser456!',
    'database': 'concesionario_motos'
}

def get_db():
    return mysql.connector.connect(**db_config)

# RUTA PRINCIPAL: LISTADO (Read)
@app.route('/')
def index():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT m.id_moto, m.modelo, m.precio, m.stock, b.nombre as marca 
        FROM motos m 
        JOIN marcas b ON m.id_marca = b.id_marca
    """
    cursor.execute(query)
    motos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', motos=motos)

# RUTA: AGREGAR (Create)
@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    if request.method == 'POST':
        cursor.execute('INSERT INTO motos (modelo, id_marca, precio, stock) VALUES (%s, %s, %s, %s)',
                       (request.form['modelo'], request.form['id_marca'], request.form['precio'], request.form['stock']))
        conn.commit()
        return redirect(url_for('index'))
    cursor.execute('SELECT * FROM marcas')
    marcas = cursor.fetchall()
    return render_template('agregar.html', marcas=marcas)

# RUTA: ELIMINAR (Delete)
@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM motos WHERE id_moto = %s', (id,))
    conn.commit()
    return redirect(url_for('index'))

# RUTA: BUSCADOR COMPLEJO (Punto Opcional B)
@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    motos = []
    if request.method == 'POST':
        criterio = request.form['criterio']
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT m.*, b.nombre as marca 
            FROM motos m 
            JOIN marcas b ON m.id_marca = b.id_marca
            WHERE m.modelo LIKE %s OR b.nombre LIKE %s
        """
        cursor.execute(query, (f"%{criterio}%", f"%{criterio}%"))
        motos = cursor.fetchall()
        cursor.close()
        conn.close()
    return render_template('buscar.html', motos=motos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
