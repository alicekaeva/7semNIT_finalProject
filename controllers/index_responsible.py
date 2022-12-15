from app import app
from flask import render_template, request, redirect, url_for, session
from utils import get_db_connection
from models.index_responsible_model import check, show_cards


@app.route('/responsible', methods=['get', 'post'])
def index_responsible():
    if not session.get('responsible'):
        return redirect(url_for('login'))

    conn = get_db_connection()
    df_table = show_cards(session['responsible'], conn)

    if request.values.get('check'):
        check(request.values.get('check'), conn)
        return redirect(url_for('index_responsible'))

    html = render_template(
        'index_responsible.html',
        len=len,
        table=df_table
    )
    return html
