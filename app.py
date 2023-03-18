from flask import Flask, render_template, request, redirect, url_for
import database_functions as db

app = Flask(__name__)

@app.route('/')
def index():
    engineers = db.get_all_engineers()

    return render_template('index.html', engineers = engineers)

@app.route('/edit/<rowid>')
def edit(rowid):
    engineer = db.get_engineer(rowid)
    return render_template('edit.html', engineer = engineer)

@app.route('/edit-engineer/<rowid>', methods=['POST'])
def edit_engineer(rowid):
    name = request.form['name']
    age = int(request.form['age']) 
    height = request.form['height']
    group = request.form['group']
    db.update_engineer(name, age, height, group, rowid)

    return redirect(url_for('index'))

@app.route('/post-engineer', methods=['POST'])
def submit():
    name = request.form['name']
    age = int(request.form['age']) 
    height = request.form['height']
    group = request.form['group']
    db.add_engineer(name, age, height, group)

    return redirect(url_for('index'))

@app.route('/delete-engineer/<rowid>')
def delete(rowid):
    db.delete_engineer(rowid)
    return redirect(url_for('index'))

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')