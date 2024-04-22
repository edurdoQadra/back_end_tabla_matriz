from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

#cargamos el achivo .env en este script
# Cargar las variables de entorno
from dotenv import load_dotenv
load_dotenv()
          
# # Crear la aplicación Flask
# app = Flask(__name__)

# Inicializar la aplicación Flask
app = Flask(__name__)
CORS(app)


# Configurar la conexión a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la extensión SQLAlchemy
db = SQLAlchemy(app)

