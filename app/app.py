from flask import Flask, jsonify
import sqlite3
import random

from flask_cors import CORS

DATABASE = 'palavras.db'

class DatabaseConnection:
    def __init__(self, database):
        self.database = database

    def __enter__(self):
        self.conn = sqlite3.connect(self.database)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.commit()
        self.conn.close()

class PalavraRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_palavras(self):
        with self.db_connection as db:
            db.cursor.execute('SELECT palavra FROM palavras')
            palavras = db.cursor.fetchall()
        return [p[0] for p in palavras]

class PalavraService:
    def __init__(self, repository):
        self.repository = repository

    def get_random_palavra(self):
        palavras = self.repository.get_palavras()
        return random.choice(palavras) if palavras else None

app = Flask(__name__)
cors = CORS(app)
db_connection = DatabaseConnection(DATABASE)
repository = PalavraRepository(db_connection)
service = PalavraService(repository)

@app.route('/random-word', methods=['GET'])
def palavra_aleatoria():
    palavra = service.get_random_palavra()
    if palavra:
        return jsonify({'word': palavra})
    return jsonify({'error': 'No words found'}), 404
