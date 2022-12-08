import pandas


def get_work(conn):
    return pandas.read_sql('SELECT * FROM work', conn)


def get_genre(conn):
    return pandas.read_sql('SELECT * FROM genre', conn)
