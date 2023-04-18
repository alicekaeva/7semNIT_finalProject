import pandas


def check(iaw_id, conn):
    cur = conn.cursor()
    cur.execute('''
    UPDATE issue_article_work
    SET checked = 1, comment = NULL
    WHERE issue_article_work_id = :id
    ''', {"id": iaw_id})
    return conn.commit()

def mistakes(iaw_id, comment, conn):
    cur = conn.cursor()
    cur.execute('''
    UPDATE issue_article_work
    SET start_date = NULL, end_date = NULL, comment = :comment
    WHERE issue_article_work_id = :id
    ''', {"id": iaw_id, "comment": comment})
    return conn.commit()

def add_to_history(iaw_id, conn):
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO history (issue_article_work_id, issue_article_id, work_id, worker_id, responsible_for_work_id, start_date, end_date, checked, comment)
    SELECT issue_article_work_id, issue_article_id, work_id, worker_id, responsible_for_work_id, start_date, end_date, checked, comment
    FROM issue_article_work
    WHERE issue_article_work_id = :id
    ''', {"id": iaw_id})
    return conn.commit()
