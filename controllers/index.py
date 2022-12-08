from app import app
from flask import render_template, request, session
from utils import get_db_connection
#from models.issues_model import


@app.route('/', methods=['get'])
def index():
    #conn = get_db_connection()

    html = render_template(
        'index.html'
    )
    return html