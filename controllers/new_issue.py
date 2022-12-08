from app import app
from flask import render_template


@app.route('/new_issue', methods=['get'])
def new_issue():
    html = render_template(
        'new_issue.html',
    )
    return html
