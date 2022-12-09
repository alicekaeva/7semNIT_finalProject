from app import app
from flask import render_template, request, session
from utils import get_db_connection
from models.edit_issue_model import get_work, get_genre, add_article, add_issue_article, add_issue_article_work


@app.route('/edit_issue', methods=['get', 'post'])
def edit_issue():
    conn = get_db_connection()
    df_works = get_work(conn)
    df_genres = get_genre(conn)
    edit_issue_name = session.get('editable')
    edit_issue_id = session.get('editable_id')

    if request.values.get('edit_issue'):
        name = request.values.get('edit_issue')
        genre_id= request.values.get('genre')
        works_ids = [int(item) for item in request.form.getlist('work')]
        article_id = add_article(name, genre_id, conn)
        issue_article_id = add_issue_article(edit_issue_id, article_id, conn)
        add_issue_article_work(issue_article_id, works_ids, conn)

    html = render_template(
        'edit_issue.html',
        f_name=edit_issue_name,
        len=len,
        works = df_works,
        genres=df_genres
    )
    return html
