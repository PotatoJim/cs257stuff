from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/rand/<low>/<high>')
def rand(low, high):
    #Input values that come from a URL (i.e., @app.route)
    #   are always strings so I need to convert the type to int
    low_int = int(low)
    high_int = int(high)
    
    num = random.randint(low_int, high_int)
    return render_template("random.html", randNum = num)

@app.route('/test')
def testThing():
    return render_template("testThing.html")

@app.route('/movie')
def movie():
    conn = psycopg2.connect(
        host = "localhost",
        port = 5432,
        database = "vilmsj",
        user = "vilmsj",
        password = "eyebrow398blue"
    )

    cur = conn.cursor()
    num = random.randint(0, 45466)
    query = f'SELECT title FROM movies'
if __name__ == '__main__':
    my_port = 5230
    app.run(host='0.0.0.0', port = my_port) 
