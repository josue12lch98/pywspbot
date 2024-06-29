


from flask import Flask
from Config import DevelopmentConfig  # Importa la configuración que necesitas

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)  # Utiliza la configuración del objeto

# Ahora inicializa SQLAlchemy con la app configurada
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

# Modelo de la tabla y otras partes de tu aplicación aquí...

# Resto del código de Flask...



with app.app_context():  # Crear la tabla si no existe
    db.create_all()
    # t1= Log(texto = "Test1")
    # t2= Log(texto = "Test2", number = "XXXXXXXXX")
    # db.session.add(t1)
    # db.session.add(t2)
    # db.session.commit()





mensajes_log = []


# Función para agregar mensajes y guardar en la base de datos





# variables globales
flow = 0
dni = ""
full_name = ""
name = ""
client = ""
sucursal = ""

# Token de verificación para la configuración
TOKEN = "TOKENX"






