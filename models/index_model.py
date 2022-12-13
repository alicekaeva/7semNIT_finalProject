import pandas


def get_workers(work_id, conn):
    return pandas.read_sql('''
    SELECT * 
    FROM worker
    JOIN work_worker USING (worker_id)
    JOIN work USING (work_id)
    WHERE work_id = :id
    ''', conn, params={"id": work_id})


def get_responsible(worker_id, conn):
    return pandas.read_sql('''
    SELECT *
    FROM worker
    WHERE worker_id IS NOT :id
    ''', conn, params={"id": worker_id})


def show_cards(conn):
    return pandas.read_sql('''
    SELECT iaw.issue_article_work_id, iaw.work_id, issue_name AS Выпуск, article_name AS Статья, work_name AS Работа, w.worker_name AS Работник, r.worker_name AS Ответственный, iaw.start_date AS Начал, iaw.end_date AS Закончил, iaw.checked AS Проверено
    FROM issue_article_work AS iaw
    JOIN issue_article USING (issue_article_id)
    JOIN issue USING (issue_id)
    JOIN article USING (article_id)
    JOIN work USING (work_id)
    LEFT JOIN worker AS w ON iaw.worker_id = w.worker_id
    LEFT JOIN worker AS r ON iaw.responsible_for_work_id = r.worker_id
    WHERE checked = 0 OR checked is NULL
    ''', conn)


def took(iaw_id, conn):
    cur = conn.cursor()
    cur.execute('''
    UPDATE issue_article_work
    SET start_date = date('now')
    WHERE issue_article_work_id = :id
    ''', {"id": iaw_id})
    return conn.commit()


def finish(iaw_id, conn):
    cur = conn.cursor()
    cur.execute('''
    UPDATE issue_article_work
    SET end_date = date('now'), checked = 0
    WHERE issue_article_work_id= :id
    ''', {"id": iaw_id})
    return conn.commit()


def check(iaw_id, conn):
    cur = conn.cursor()
    cur.execute('''
    UPDATE issue_article_work
    SET checked = 1
    WHERE issue_article_work_id = :id
    ''', {"id": iaw_id})
    return conn.commit()


def add_worker(iaw_id, w_id, conn):
    cur = conn.cursor()
    cur.execute('''
    UPDATE issue_article_work
    SET worker_id = :w_id
    WHERE issue_article_work_id = :id
    ''', {"id": iaw_id, "w_id": w_id})
    return conn.commit()


def add_res(iaw_id, r_id, conn):
    cur = conn.cursor()
    cur.execute('''
    UPDATE issue_article_work
    SET responsible_for_work_id = :r_id
    WHERE issue_article_work_id = :id
    ''', {"id": iaw_id, "r_id": r_id})
    return conn.commit()
