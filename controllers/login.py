from app import app
from flask import render_template, redirect, request, session, url_for
from models.index_worker_model import get_worker
from utils import get_db_connection


@app.route('/login', methods=['get', 'post'])
def login():
    check = 0
    err = 0
    conn = get_db_connection()

    if request.values.get('role') == 'admin':
        session['admin'] = 'admin'
        return redirect(url_for('index'))
    elif request.values.get('role') == 'worker' and not request.values.get('name'):
        check = 1
    elif request.values.get('role') == 'responsible' and not request.values.get('name'):
        check = 2
    elif request.values.get('role') == 'worker' and request.values.get('name'):
        try:
            worker_id = int(get_worker(request.values.get('name'), conn).loc[0, "worker_id"])
            session['worker'] = worker_id
            return redirect(url_for('index_worker'))
        except KeyError:
            err = 1
    elif request.values.get('role') == 'responsible' and request.values.get('name'):
        try:
            responsible_id = int(get_worker(request.values.get('name'), conn).loc[0, "worker_id"])
            session['responsible'] = responsible_id
            return redirect(url_for('index_responsible'))
        except KeyError:
            err = 1

    return render_template('login.html', flag=check, messasge=err)
