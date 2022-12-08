from app import app
from flask import render_template, request, session
from utils import get_db_connection
from models.edit_issue_model import get_work, get_genre


@app.route('/edit_issue', methods=['get', 'post'])
def edit_issue():
    conn = get_db_connection()
    df_works = get_work(conn)
    df_genres = get_genre(conn)
    if request.values.get('genre'):
        genre_id = int(request.values.get('genre'))
        session['genre_id'] = genre_id
    else:
        session['genre_id'] = 1
    name = session.get('editable')
    html = render_template(
        'edit_issue.html',
        f_name=name,
        len=len,
        works = df_works,
        genres=df_genres
    )
    return html
