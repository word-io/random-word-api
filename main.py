from app.create_db import create_db
from app.app import app

if __name__ == '__main__':
    create_db()
    
    app.run(debug=True)
