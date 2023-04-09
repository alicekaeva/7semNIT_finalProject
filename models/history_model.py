import pandas


def get_history(conn, id):
    return pandas.read_sql(f'''
        SELECT article_name AS Статья, work_name AS Работа, w.worker_name AS Работник, r.worker_name AS Ответственный, start_date AS Начал, end_date AS Закончил, comment AS Замечание, checked AS Готово
        FROM history AS iaw
        LEFT JOIN worker AS w ON iaw.worker_id = w.worker_id
        LEFT JOIN worker AS r ON iaw.responsible_for_work_id = r.worker_id
        JOIN issue_article USING (issue_article_id)
        JOIN article USING (article_id)
        JOIN issue USING (issue_id)
        JOIN work USING (work_id)
        WHERE issue_article_work_id = :id
            ''', conn, params={"id": id})
