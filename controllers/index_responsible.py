from app import app
from flask import render_template, request, redirect, url_for, session
from utils import get_db_connection
from models.index_responsible_model import check, mistakes, add_to_history
from models.index_model import show_cards


@app.route('/responsible', methods=['get', 'post'])
def index_responsible():
    if not session.get('responsible'):
        return redirect(url_for('login'))

    conn = get_db_connection()
    df_table = show_cards(conn, responsible=session['responsible'])

    if request.values.get('ok'):
        check(request.values.get('ok'), conn)
        add_to_history(request.values.get('ok'), conn)
        return redirect(url_for('index_responsible'))
    if request.values.get('mistakes'):
        mistakes(request.values.get('id'), request.values.get('mistakes'), conn)
        add_to_history(request.values.get('id'), conn)
        return redirect(url_for('index_responsible'))

    html = render_template(
        'index.html',
        len=len,
        table=df_table,
        user='responsible'
    )
    return html
