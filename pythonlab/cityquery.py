
# We use the psycopg2 library to help us connec to the Postgres SQL database
# This library is already installed on stearns.mathcs.carleton.edu
import psycopg2

# This function tests to make sure that you can connect to the database
def test_connection():

    # You will need to change the Port and the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="vilmsj",
        user="vilmsj",
        password="eyebrow398blue")

    if conn is not None:
        print( "Connection Worked!" )
    else:
        print( "Problem with Connection" )

    return None


# This function sends an SQL query to the database
def query_one():

    # You will need to change the Port and the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="vilmsj",
        user="vilmsj",
        password="eyebrow398blue")

    cur = conn.cursor()

    sql = "SELECT * FROM cities WHERE city LIKE 'Northfield'"
    
    cur.execute( sql )

    # fetchone() returns one row that matches your quer
    row = cur.fetchone()
    if row == None:
        print("Northfield not in database")
    else:
        sql = "SELECT lat FROM row"
        cur.execute()
        lat = cur.fetchone()
        sql = "SELECT long FROM row"
        cur.execute()
        long = cur.fetchone()
        print(lat)
        print(long)


    conn.commit()
    
    
    return row

# This function sends an SQL query to the database
def query_two():

    # You will need to change the Port and the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="vilmsj",
        user="vilmsj",
        password="eyebrow398blue")

    cur = conn.cursor()

    sql = "SELECT * FROM cities ORDER BY pop"
    
    cur.execute( sql )

    # fetchone() returns one row that matches your quer
    row = cur.fetchone()
    sql = "SELECT city FROM row"
    cur.execute( sql )
    city = cur.fetchone()
    print(city)


    conn.commit()
    
    
    return row



query_one()
query_two()