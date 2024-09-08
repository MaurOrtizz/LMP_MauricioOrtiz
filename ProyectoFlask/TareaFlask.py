from flask import Flask, render_template, request, redirect, url_for
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
    cursor = db.cursor(dictionary=True)
    
    if request.method == 'POST':
        id = request.form.get('id')
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        correo = request.form.get('correo')
        cursor = db.cursor()
        if id:
            cursor.execute("UPDATE usuarios SET nombre = %s, apellido = %s, correo = %s WHERE id = %s", (nombre, apellido, correo, id))
            db.commit()
        else:
            cursor.execute("INSERT INTO usuarios (nombre, apellido, correo) VALUES (%s, %s, %s)", (nombre, apellido, correo))
            db.commit()
        return redirect(url_for('Index'))
    
    edit = None
    if request.args.get('edit'):
        id = request.args.get('edit')
        cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
        edit = cursor.fetchone()
    
    if request.args.get('delete'):
        id = request.args.get('delete')
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
        db.commit()
    
    cursor.execute("SELECT * FROM usuarios")
    datos = cursor.fetchall()
    cursor.close()
    
    return render_template('form.html', usuarios = datos, edit = edit)

if __name__ == "__main__":
    app.run(debug=True)