import pandas


def start(iaw_id, conn):
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


def get_worker(name, conn):
    return pandas.read_sql('''
    SELECT worker_id
    FROM worker
    WHERE worker_name = :name
    ''', conn, params={"name": name})
