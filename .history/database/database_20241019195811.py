import sqlite3

DB_NAME = "todo_list.db"

def connect_db():
  conn = sqlite3.connect(DB_NAME)  #* Connect to the database
  cur = conn.cursor()  #* We using this to manipulate with query in database
  cur.execute('''
              CREATE TABLE IF NOT EXISTS tasks
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
              )
              ''')
  