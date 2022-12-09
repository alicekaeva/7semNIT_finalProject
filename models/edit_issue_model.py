import pandas


def get_work(conn):
    return pandas.read_sql('SELECT * FROM work', conn)


def get_genre(conn):
    return pandas.read_sql('SELECT * FROM genre', conn)


def add_article(name, genre, conn):
    cur = conn.cursor()
    cur.execute('INSERT INTO article(article_name, genre_id) VALUES (:new_article, :new_genre_id)',
                {"new_article": name, "new_genre_id": genre})
    conn.commit()
    return cur.lastrowid


def add_issue_article(issue, article, conn):
    cur = conn.cursor()
    cur.execute('INSERT INTO issue_article(issue_id, article_id) VALUES (:new_issue, :new_article)',
                {"new_issue": issue, "new_article": article})
    conn.commit()
    return cur.lastrowid


def add_issue_article_work(issue_article, works, conn):
    cur = conn.cursor()
    for item in works:
        cur.execute('''INSERT INTO issue_article_work(issue_article_id, work_id, worker_id, responsible_for_work_id, 
        start_date, end_date, checked) VALUES (:new_issue_article, :new_work, NULL, NULL, NULL, NULL, NULL)''',
                    {"new_issue_article": issue_article, "new_work": item})
    return conn.commit()


def show_edit_table(id, conn):
    return pandas.read_sql('''
    SELECT article_name AS Статья, genre_name AS Жанр, GROUP_CONCAT(work_name,', ') AS Работы
    FROM issue_article_work
    JOIN issue_article USING (issue_article_id)
    JOIN article USING (article_id)
    JOIN work USING (work_id)
    JOIN genre USING (genre_id)
    JOIN issue USING (issue_id)
    WHERE issue_id = :id
    GROUP BY  issue_article_id
    ''', conn, params={"id": id})
