from app import app
from flask import render_template, request, session, redirect, url_for
from utils import get_db_connection
from models.issues_model import get_issues, add_issue, show_table, show_dealine
import datetime


@app.route('/issues', methods=['get', 'post'])
def issues():
    conn = get_db_connection()
    check = 0

    if request.values.get('new_issue'):
        new_issue = request.values.get('new_issue')
        new_date = request.values.get('new_date')
        session['id'] = add_issue(new_issue, new_date, conn)
    elif request.values.get('editable'):
        session['editable'] = request.values.get('editable')
        session['editable_id'] = int(request.values.get('editable_id'))
        return redirect(url_for('edit_issue'))
    elif request.values.get('issue'):
        id = int(request.values.get('issue'))
        session['id'] = id

    df_issues = get_issues(conn)
    df_table = show_table(session['id'], conn)
    deadline = show_dealine(session['id'], conn).loc[0, "deadline"]

    if deadline < str(datetime.datetime.now().date()):
        check = 1
    print(check)

    html = render_template(
        'issues.html',
        len=len,
        issue=df_issues,
        table=df_table,
        id=session['id'],
        flag=check,
        deadline=deadline
    )
    return html
