from flask import Blueprint

cursos_bp = Blueprint('cursos', __name__)


@cursos_bp.route('/')
def index():
    return 'cursos'


@cursos_bp.route('/pagina')
def page():
    return 'pagina'
