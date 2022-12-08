import pandas


def get_issues(conn):
    return pandas.read_sql('SELECT * FROM issue', conn)


def add_issue(name, date, conn):
    cur = conn.cursor()
    cur.execute('INSERT INTO issue(issue_name, deadline) VALUES (:new_issue, :new_date)',
                {"new_issue": name, "new_date": date})
    return conn.commit()
