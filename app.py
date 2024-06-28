


from flask import Flask
from Config import DevelopmentConfig  # Importa la configuración que necesitas

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)  # Utiliza la configuración del objeto

# Ahora inicializa SQLAlchemy con la app configurada
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

# Modelo de la tabla y otras partes de tu aplicación aquí...

# Resto del código de Flask...


app = Flask(__name__)

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///metapython.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Modelo de la tabla log


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






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
    # app.run(debug=True)

# Commands to push to production
# git add .
# git commit -m "xxx"
#  git push