from app import app
from flask import render_template, request, redirect, url_for, session
from utils import get_db_connection
from models.index_worker_model import start, finish, show_cards


@app.route('/worker', methods=['get', 'post'])
def index_worker():
    if not session.get('worker'):
        return redirect(url_for('login'))

    conn = get_db_connection()
    df_table = show_cards(session['worker'], conn)

    if request.values.get('start'):
        start(request.values.get('start'), conn)
        return redirect(url_for('index_worker'))
    elif request.values.get('finish'):
        finish(request.values.get('finish'), conn)
        return redirect(url_for('index_worker'))

    html = render_template(
        'index_worker.html',
        len=len,
        table=df_table
    )
    return html
