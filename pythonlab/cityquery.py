
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

    sql = "SELECT latitude, longitude FROM cities WHERE city LIKE 'Northfield'"
    
    cur.execute( sql )

    # fetchone() returns one row that matches your quer
    row = cur.fetchone()
    if row == None:
        print("Northfield not in database")
    else:
        print(row)


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

    sql = "SELECT city FROM cities ORDER BY pop DESC"
    cur.execute( sql )
    city = cur.fetchone()
    print(city)


    conn.commit()
    
    
    return city


# This function sends an SQL query to the database
def query_three():

    # You will need to change the Port and the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="vilmsj",
        user="vilmsj",
        password="eyebrow398blue")

    cur = conn.cursor()

    sql = "SELECT city FROM cities WHERE state LIKE 'Minnesota' ORDER BY pop ASC"
    cur.execute( sql )
    city = cur.fetchone()
    print(city)


    conn.commit()
    
    
    return city

def query_three():

    # You will need to change the Port and the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="vilmsj",
        user="vilmsj",
        password="eyebrow398blue")

    cur = conn.cursor()
    #furthest north
    sql = "SELECT city FROM cities ORDER BY longitude ASC"
    cur.execute( sql )
    city = cur.fetchone()
    print(city)
    #furthest east
    sql = "SELECT city FROM cities ORDER BY latitude ASC"
    cur.execute( sql )
    city = cur.fetchone()
    print(city)
    #furthest south
    sql = "SELECT city FROM cities ORDER BY longitude DESC"
    cur.execute( sql )
    city = cur.fetchone()
    print(city)
    #furthest west
    sql = "SELECT city FROM cities ORDER BY latitude DESC"
    cur.execute( sql )
    city = cur.fetchone()
    print(city)

    conn.commit()
    
    
    return city

query_one()
query_two()
query_three()