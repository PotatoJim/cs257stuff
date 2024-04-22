
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

    sql = "SELECT lat, long FROM cities WHERE city LIKE 'Northfield'"
    
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

    sql = "SELECT city FROM cities ORDER BY pop"
    cur.execute( sql )
    city = cur.fetchone()
    print(city)


    conn.commit()
    
    
    return city



query_one()
query_two()