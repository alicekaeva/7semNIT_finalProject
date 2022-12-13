from app import app
from flask import render_template, request, session
from utils import get_db_connection
from models.index_model import show_cards, get_workers, get_responsible, add_worker, add_res


@app.route('/', methods=['get', 'post'])
def index():
    conn = get_db_connection()
    df_table = show_cards(conn)

    if request.values.get('worker'):
        session['worker_id'] = int(request.values.get('worker'))
        add_worker(request.values.get('w_iaw'), session['worker_id'], conn)
    elif request.values.get('res'):
        session['res_id'] = int(request.values.get('res'))
        add_res(request.values.get('issue_article_work_id'), session['res_id'], conn)
    else:
        session['worker_id'] = 1
        session['work_id'] = 1

    df_w = get_workers(session['work_id'], conn)
    df_r = get_responsible(session['worker_id'], conn)

    html = render_template(
        'index.html',
        table=df_table,
        len=len,
        w=df_w,
        r=df_r
    )
    return html
