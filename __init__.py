from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Config import Config

# Inicializa las extensiones sin pasar la instancia de la aplicación
db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializar extensiones con la aplicación creada
    db.init_app(app)

    # Importa e registra los blueprints
    from app import main
    app.register_blueprint(main)

    return app
