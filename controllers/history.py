from app import app
from flask import render_template, session
from utils import get_db_connection
from models.history_model import get_history


@app.route('/history', methods=['get', 'post'])
def history():
    conn = get_db_connection()
    iaw_id = session.get('iaw_id')
    df_table = get_history(conn, iaw_id)

    html = render_template(
        'history.html',
        table=df_table,
        len=len
    )
    return html
