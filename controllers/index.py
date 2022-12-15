from app import app
from flask import render_template, request, redirect, url_for, session
from utils import get_db_connection
from models.index_model import show_cards


@app.route('/', methods=['get', 'post'])
def index():
    if not session.get('admin'):
        return redirect(url_for('login'))

    conn = get_db_connection()
    df_table = show_cards(conn)

    if request.values.get('iaw_id'):
        session['iaw_id'] = int(request.values.get('iaw_id'))
        session['w_id'] = int(request.values.get('w_id'))
        session['check'] = 0
        return redirect(url_for('edit_work'))

    html = render_template(
        'index.html',
        table=df_table,
        len=len
    )
    return html
