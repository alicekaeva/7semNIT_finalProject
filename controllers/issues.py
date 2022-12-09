from app import app
from flask import render_template, request, session, redirect, url_for
from utils import get_db_connection
from models.issues_model import get_issues, add_issue


@app.route('/issues', methods=['get', 'post'])
def issues():
    conn = get_db_connection()

    if request.values.get('new_issue'):
        new_issue = request.values.get('new_issue')
        new_date = request.values.get('new_date')
        add_issue(new_issue, new_date, conn)
    elif request.values.get('editable'):
        session['editable'] = request.values.get('editable')
        session['editable_id'] = int(request.values.get('editable_id'))
        return redirect(url_for('edit_issue'))

    df_issues = get_issues(conn)

    html = render_template(
        'issues.html',
        len=len,
        issue=df_issues
    )
    return html