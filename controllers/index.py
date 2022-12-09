from app import app
from flask import render_template, request, session
from utils import get_db_connection
from models.index_model import show_cards, get_workers


@app.route('/', methods=['get'])
def index():
    conn = get_db_connection()
    df_table = show_cards(conn)

    html = render_template(
        'index.html',
        table=df_table,
        len=len
    )
    return html
