
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
    print("City with Largest Pop.:")
    print(city[0])


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
    print("City in MN with Smallest Pop.:")
    print(city[0])


    conn.commit()
    
    
    return city

def query_four():

    # You will need to change the Port and the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="vilmsj",
        user="vilmsj",
        password="eyebrow398blue")

    cur = conn.cursor()

    #furthest north
    sql = "SELECT city FROM cities ORDER BY latitude DESC"
    cur.execute( sql )
    city = cur.fetchone()
    print("Furthest North:")
    print(city[0])

    #furthest East
    sql = "SELECT city FROM cities ORDER BY longitude DESC"
    cur.execute( sql )
    city = cur.fetchone()
    print("Furthest East:")
    print(city[0])

    #furthest south
    sql = "SELECT city FROM cities ORDER BY latitude ASC"
    cur.execute( sql )
    city = cur.fetchone()
    print("Furthest South:")
    print(city[0])

    #furthest west
    sql = "SELECT city FROM cities ORDER BY longitude ASC"
    cur.execute( sql )
    city = cur.fetchone()
    print("Furthest West:")
    print(city[0])

    conn.commit()
    
    
    return city

# This function sends an SQL query to the database
def query_five():

    # You will need to change the Port and the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="vilmsj",
        user="vilmsj",
        password="eyebrow398blue")

    cur = conn.cursor()
    state = input("Enter a State:")
    if len(state) == 2:
        state = state.upper()
        stateLookup = f'SELECT state FROM states WHERE code LIKE \'{state}\''
        cur.execute(stateLookup)
        state = cur.fetchone()[0]

    else:
        state = state.capitalize()
    
    if state == None:
        print("State Invalid")
        return 0

    sql = f'SELECT city FROM cities WHERE state LIKE \'{state}\''
    cur.execute( sql )
    cities = cur.fetchall()
    if cities == None:
        print("State Invalid")
        return 0
    else:
        print(f'Cities in {state}')
        for i in cities:
            print(f' - {i[0]}')


    conn.commit()
    
    
    return 1

query_one()
query_two()
query_three()
query_four()
query_five()