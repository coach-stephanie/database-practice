from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    engineers = get_all_engineers()

    return render_template('index.html', engineers = engineers)

@app.route('/success', methods=['POST'])
def submit():
    name = request.form['name']
    age = int(request.form['age']) 
    height = request.form['height']
    group = request.form['group']
    add_engineer(name, age, height, group)

    return render_template('success.html')

def add_engineer(name, age, height, group):
    conn = sqlite3.connect('./static/data/team-edge.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO engineers(name, age, height, group_num) VALUES (?, ?, ?, ?)", (name, age, height, group))
    conn.commit()
    conn.close()

def get_all_engineers():
    conn = sqlite3.connect('./static/data/team-edge.db')
    curs = conn.cursor()
    result = curs.execute("SELECT * FROM engineers")
    engineers = []

    for row in result: 
        engineer = {
            'name': row[0],
            'age': row[1],
            'height': row[2],
            'group': row[3]
        }
        engineers.append(engineer)

    conn.close()
    return engineers

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')