import pandas


# def took(id, conn):
#     cur = conn.cursor()
#     cur.execute('''
#     UPDATE issues_article_work
#     SET start_date = date('now')
#     WHERE worker_id = :id
#     ''', {"id": id})
#     return conn.commit()


def get_workers(work_name, conn):
    return pandas.read_sql('''
    SELECT * 
    FROM worker
    JOIN work_worker USING (worker_id)
    WHERE work_name = :name
    ''', conn, params={"name": work_name})


def get_responsible(worker_id, conn):
    return pandas.read_sql('''
    SELECT * 
    FROM worker
    WHERE worker_id IS NOT :id
    ''', conn, params={"id": worker_id})


def check(iaw_id, conn):
    cur = conn.cursor()
    cur.execute('''
    UPDATE issues_article_work
    SET checked = 1
    WHERE issue_article_work_id = :id
    ''', {"id": iaw_id})
    return conn.commit()


def show_cards(conn):
    return pandas.read_sql('''
    SELECT issue_name AS Выпуск, article_name AS Статья, work_name AS Работа, worker_name AS Работник, worker_name AS Ответственный, start_date AS Начал, end_date AS Закончил, checked AS Проверено
    FROM issue_article_work
    JOIN issue_article USING (issue_article_id)
    JOIN issue USING (issue_id)
    JOIN article USING (article_id)
    JOIN work USING (work_id)
    LEFT JOIN worker USING (worker_id)
    ''', conn)
