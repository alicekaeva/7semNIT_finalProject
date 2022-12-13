import pandas


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
