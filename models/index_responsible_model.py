import pandas


def check(iaw_id, conn):
    cur = conn.cursor()
    cur.execute('''
    UPDATE issue_article_work
    SET checked = 1
    WHERE issue_article_work_id = :id
    ''', {"id": iaw_id})
    return conn.commit()


def show_cards(id, conn):
    return pandas.read_sql('''
    SELECT iaw.issue_article_work_id, iaw.work_id, issue_name AS Выпуск, article_name AS Статья, work_name AS Работа, w.worker_name AS Работник, r.worker_name AS Ответственный, iaw.start_date AS Начал, iaw.end_date AS Закончил, iaw.checked AS Проверено
    FROM issue_article_work AS iaw
    JOIN issue_article USING (issue_article_id)
    JOIN issue USING (issue_id)
    JOIN article USING (article_id)
    JOIN work USING (work_id)
    LEFT JOIN worker AS w ON iaw.worker_id = w.worker_id
    LEFT JOIN worker AS r ON iaw.responsible_for_work_id = r.worker_id
    WHERE checked = 0 and deadline > date('now') and responsible_for_work_id = :id
    ''', conn, params={"id": id})
