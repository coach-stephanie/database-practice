from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    engineers = get_all_engineers()

    return render_template('index.html', engineers = engineers)

@app.route('/edit/<rowid>')
def edit(rowid):
    engineer = get_engineer(rowid)
    return render_template('edit.html', engineer = engineer)

@app.route('/edit-engineer/<rowid>', methods=['POST'])
def edit_engineer(rowid):
    name = request.form['name']
    age = int(request.form['age']) 
    height = request.form['height']
    group = request.form['group']
    update_engineer(name, age, height, group, rowid)

    return redirect(url_for('index'))

@app.route('/post-engineer', methods=['POST'])
def submit():
    name = request.form['name']
    age = int(request.form['age']) 
    height = request.form['height']
    group = request.form['group']
    add_engineer(name, age, height, group)

    return redirect(url_for('index'))

@app.route('/delete-engineer/<rowid>')
def delete(rowid):
    delete_engineer(rowid)
    return redirect(url_for('index'))

def add_engineer(name, age, height, group):
    conn = sqlite3.connect('./static/data/team-edge.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO engineers(name, age, height, group_num) VALUES (?, ?, ?, ?)", (name, age, height, group))
    conn.commit()
    conn.close()

def update_engineer(name, age, height, group, rowid):
    conn = sqlite3.connect('./static/data/team-edge.db')
    curs = conn.cursor()
    curs.execute("UPDATE engineers SET name = ?, age = ?, height = ?, group_num = ? WHERE rowid = ?", (name, age, height, group, rowid))
    conn.commit()
    conn.close()

def delete_engineer(rowid):
    conn = sqlite3.connect('./static/data/team-edge.db')
    curs = conn.cursor()
    curs.execute("DELETE FROM engineers WHERE rowid = ?", (rowid,))
    conn.commit()
    conn.close()

def get_engineer(rowid):
    conn = sqlite3.connect('./static/data/team-edge.db')
    curs = conn.cursor()
    result = curs.execute("SELECT rowid, * FROM engineers WHERE rowid = ?", (rowid,))
    engineer = {}

    for row in result: 
        engineer = {
            'rowid': row[0],
            'name': row[1],
            'age': row[2],
            'height': row[3],
            'group': row[4]
        }

    conn.close()
    return engineer

def get_all_engineers():
    conn = sqlite3.connect('./static/data/team-edge.db')
    curs = conn.cursor()
    result = curs.execute("SELECT rowid, * FROM engineers")
    engineers = []

    for row in result: 
        engineer = {
            'rowid': row[0],
            'name': row[1],
            'age': row[2],
            'height': row[3],
            'group': row[4]
        }
        engineers.append(engineer)

    conn.close()
    return engineers

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')