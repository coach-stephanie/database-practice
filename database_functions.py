import sqlite3

database = './static/data/team-edge.db'

def add_engineer(name, age, height, group):
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    curs.execute("INSERT INTO engineers(name, age, height, group_num) VALUES (?, ?, ?, ?)", (name, age, height, group))
    conn.commit()
    conn.close()

def update_engineer(name, age, height, group, rowid):
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    curs.execute("UPDATE engineers SET name = ?, age = ?, height = ?, group_num = ? WHERE rowid = ?", (name, age, height, group, rowid))
    conn.commit()
    conn.close()

def delete_engineer(rowid):
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    curs.execute("DELETE FROM engineers WHERE rowid = ?", (rowid,))
    conn.commit()
    conn.close()

def get_engineer(rowid):
    conn = sqlite3.connect(database)
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
    conn = sqlite3.connect(database)
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