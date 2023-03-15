from app import app
from flask import render_template, redirect, request, session, url_for
from models.index_worker_model import get_worker
from utils import get_db_connection


@app.route('/login', methods=['get', 'post'])
def login():
    check = 0
    err = 0
    conn = get_db_connection()

    if request.values.get('admin'):
        session['admin'] = request.form.get('admin')
        return redirect(url_for('index'))
    elif request.values.get('worker') and not request.values.get('name'):
        session['worker'] = request.form.get('worker')
        check = 1
    elif request.values.get('responsible') and not request.values.get('name'):
        session['responsible'] = request.form.get('responsible')
        check = 2
    elif request.values.get('worker') and request.values.get('name'):
        try:
            worker_id = int(get_worker(request.values.get('name'), conn).loc[0, "worker_id"])
            session['worker'] = worker_id
            return redirect(url_for('index_worker'))
        except KeyError:
            err = 1
    elif request.values.get('responsible') and request.values.get('name'):
        try:
            responsible_id = int(get_worker(request.values.get('name'), conn).loc[0, "worker_id"])
            session['responsible'] = responsible_id
            return redirect(url_for('index_responsible'))
        except KeyError:
            err = 1

    return render_template('login.html', flag=check, messasge=err)
