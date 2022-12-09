import pandas


def get_issues(conn):
    return pandas.read_sql('SELECT * FROM issue', conn)


def add_issue(name, date, conn):
    cur = conn.cursor()
    cur.execute('INSERT INTO issue(issue_name, deadline) VALUES (:new_issue, :new_date)',
                {"new_issue": name, "new_date": date})
    return conn.commit()


def show_table(id, conn):
    return pandas.read_sql('''
    SELECT article_name AS Статья, work_name AS Работа, worker_name AS Работник, worker_name AS Ответственный, start_date AS Начал, end_date AS Закончил, checked AS Проверено
    FROM issue_article_work
    LEFT JOIN worker USING (worker_id)
    JOIN issue_article USING (issue_article_id)
    JOIN article USING (article_id)
    JOIN issue USING (issue_id)
    JOIN work USING (work_id)
    WHERE issue_id = :id
    ''', conn, params={"id": id})
