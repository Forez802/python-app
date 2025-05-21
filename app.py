from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='mysql',
        user='sumauser',
        password='sumapass',
        database='sumadb'
    )

@app.route('/sumar', methods=['POST'])
def sumar():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    resultado = a + b

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO resultados (a, b, resultado) VALUES (%s, %s, %s)", (a, b, resultado))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
