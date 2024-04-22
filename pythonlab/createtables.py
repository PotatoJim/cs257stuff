import psycopg2

def makeTable1():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="vilmsj",
        user="vilmsj",
        password="eyebrow398blue")

    cur = conn.cursor()

    sql = "CREATE TABLE cities (city text, state text, pop real, latitude real, longitude real)"

    cur.execute( sql )

    conn.commit()

    return 1

def makeTable2():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="vilmsj",
        user="vilmsj",
        password="eyebrow398blue")

    cur = conn.cursor()

    sql = "CREATE TABLE states (code text, state text, pop real)"

    cur.execute( sql )

    conn.commit()

    return 1

makeTable1()
makeTable2()