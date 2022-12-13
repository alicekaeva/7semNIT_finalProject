from app import app
from flask import render_template, session, request, redirect, url_for
from utils import get_db_connection
from models.edit_work_model import add_res, add_worker, get_workers, get_responsible


@app.route('/edit_work', methods=['get', 'post'])
def edit_work():
    conn = get_db_connection()
    iaw_id = session.get('iaw_id')
    w_id = session.get('w_id')
    df_w = get_workers(w_id, conn)
    df_r = get_responsible(session['worker'], conn)

    if request.values.get('worker'):
        session['worker'] = int(request.values.get('worker'))
        add_worker(iaw_id, session['worker'], conn)
        session['check']  = 1
        return redirect(url_for('edit_work'))
    elif request.values.get('res'):
        add_res(iaw_id, request.values.get('res'), conn)
        return redirect(url_for('index'))
    else:
        session['worker'] = 1

    html = render_template(
        'edit_work.html',
        len=len,
        worker=df_w,
        res=df_r,
        flag=session['check']
    )
    return html
