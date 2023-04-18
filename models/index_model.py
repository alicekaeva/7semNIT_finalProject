import pandas


def show_cards(conn, worker=None, responsible=None):
    query = '''
    SELECT iaw.issue_article_work_id, iaw.work_id, issue_name AS Выпуск, article_name AS Статья, work_name AS Работа, w.worker_name AS Работник, r.worker_name AS Ответственный, iaw.start_date AS Начал, iaw.end_date AS Закончил, iaw.comment AS Замечание, iaw.checked AS Готово
    FROM issue_article_work AS iaw
    JOIN issue_article USING (issue_article_id)
    JOIN issue USING (issue_id)
    JOIN article USING (article_id)
    JOIN work USING (work_id)
    LEFT JOIN worker AS w ON iaw.worker_id = w.worker_id
    LEFT JOIN worker AS r ON iaw.responsible_for_work_id = r.worker_id
    WHERE deadline > date('now')
    '''
    if worker is not None:
        query += ' and iaw.worker_id = :id and iaw.checked = 0'
        params = {"id": worker}
    elif responsible is not None:
        query += ' and iaw.responsible_for_work_id = :responsible and iaw.checked = 0'
        params = {"responsible": responsible}
    else:
        params = None

    return pandas.read_sql(query, conn, params=params)
