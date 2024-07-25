from flask import Flask, jsonify
import sqlite3
import random

app = Flask(__name__)

def get_palavras():
    conn = sqlite3.connect('palavras.db')
    cursor = conn.cursor()
    cursor.execute('SELECT palavra FROM palavras')
    palavras = cursor.fetchall()
    conn.close()
    return [p[0] for p in palavras]

@app.route('/random-word', methods=['GET'])
def palavra_aleatoria():
    palavras = get_palavras()
    palavra = random.choice(palavras)
    return jsonify({'palavra': palavra})

if __name__ == '__main__':
    app.run(debug=True)
