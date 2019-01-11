from flask import Flask
from .cursos import cursos_bp


app = Flask(__name__)

app.register_blueprint(cursos_bp, url_prefix='/cursos')
