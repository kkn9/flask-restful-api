from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    db.init_app(app)
    
    return app

if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)