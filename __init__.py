from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Config import Config


db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    from dbQuery import UserState
    with app.app_context():  # Crear la tabla si no existe
        db.create_all()
    # Importar y usar las vistas directamente
    import routes # Suponiendo que `routes.py` esté en el mismo nivel que `__init__.py`

    routes.init_app(app)  # Esta función definirá todas las rutas

    return app