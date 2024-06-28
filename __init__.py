from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    # Importar y usar las vistas directamente
    from app import routes  # Suponiendo que `routes.py` esté en el mismo nivel que `__init__.py`

    routes.init_app(app)  # Esta función definirá todas las rutas

    return app
