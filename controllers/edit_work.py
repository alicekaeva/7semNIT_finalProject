from app import app
from flask import render_template
from utils import get_db_connection
from models.edit_work_model import add_res, add_worker


@app.route('/edit_work', methods=['get', 'post'])
def edit_work():
    conn = get_db_connection()

    html = render_template(
        'edit_work.html'
    )
    return html
