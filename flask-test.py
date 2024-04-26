import flask

app = flask.Flask(__name__)

#
@app.route('/hello')
def my_function():
    return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:Red">' + word1 + '</h1>'


@app.route('/add/<num1>/<num2>')
def my_sum(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    sum = num1 + num2
    return f'{num1} + {num2} = ' + '<h1 style="color:Red">' + f'{sum}' + '</h1>'


@app.route('/pop/<abbrev>')
def my_pop(abbrev):
    conn = psycopg2.connect(
        host ="localhost",
        port=5432,
        database="vilmsj",
        user="vilmsj",
        password="eyebrow398blue"
    )
    cur = conn.cursor()
    abbrev = abbrev.upper()
    stateLookup = f'SELECT pop FROM states WHERE code LIKE \'{abbrev}\''
    cur.execute(stateLookup)
    pop = cur.fetchone()
    if pop == None:
        return "Invalid State Code"
    
    pop = pop[0]
    return pop



if __name__ == '__main__':
    my_port = 5130
    app.run(host='0.0.0.0', port = my_port) 
