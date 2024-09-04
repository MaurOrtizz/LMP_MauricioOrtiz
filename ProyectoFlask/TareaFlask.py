from flask import Flask, render_template, request, redirect
import mysql.connector
import mysql.connector.cursor

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tareafl1",
    port="3307"
)

if(db.is_connected):
    print("Si se pudo")
else:
    print("No se pudo")


@app.route('/', methods=['POST', 'GET'])
def Index():

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        correo = request.form.get('correo')
        cursor = db.cursor()

        cursor.execute("INSERT INTO usuarios (nombre, apellido, correo) VALUES (%s, %s, %s)", (nombre, apellido, correo))
        db.commit()
        cursor.close()

    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios")
    datos = cursor.fetchall()
    cursor.close()
    
    return render_template('form.html', usuarios = datos)

'''@app.route('/submit', methods=['POST'])
def submit():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    correo = request.form['correo']

    cursor = db.cursor()
    query = "INSERT INTO usuarios (nombre, apellido, correo) VALUES (%s, %s, %s)"
    values = (nombre, apellido, correo)
    cursor.execute(query, values)
    db.commit()

    cursor.close()

    return f"Datos recibidos: Nombre: {nombre}, Apellido: {apellido}, Correo: {correo}"'''



if __name__ == "__main__":
    app.run(debug=True)