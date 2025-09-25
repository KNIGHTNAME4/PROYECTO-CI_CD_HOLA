from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Ruta principal
@app.route("/")
def index():
    conn = sqlite3.connect('database/database.db')
    c = conn.cursor()
    # Crear tabla si no existe
    c.execute('CREATE TABLE IF NOT EXISTS feedback(id INTEGER PRIMARY KEY, message TEXT)')
    # Insertar un feedback de ejemplo
    c.execute("INSERT INTO feedback(message) VALUES('Feedback continuo activado')")
    conn.commit()
    c.execute("SELECT * FROM feedback")
    data = c.fetchall()
    conn.close()
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
