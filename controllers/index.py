from app import app
from flask import render_template, request, session,redirect, url_for
from utils import get_db_connection
from models.index_model import show_cards, start, finish, check


@app.route('/', methods=['get', 'post'])
def index():
    conn = get_db_connection()
    df_table = show_cards(conn)

    if request.values.get('start'):
        start(request.values.get('start'), conn)
        return redirect(url_for('index'))
    elif request.values.get('finish'):
        finish(request.values.get('finish'), conn)
        return redirect(url_for('index'))
    elif request.values.get('check'):
        check(request.values.get('check'), conn)
        return redirect(url_for('index'))


    html = render_template(
        'index.html',
        table=df_table,
        len=len
    )
    return html
