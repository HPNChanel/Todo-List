import sqlite3

DB_NAME = "todo_list.db"

def connect_db():
  conn = sqlite3.connect(DB_NAME)  #* Connect to the database
  cur = conn.cursor()  #* We using this to manipulate with query in database
  cur.execute('''
              CREATE TABLE IF NOT EXISTS tasks
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
              task TEXT NOT NULL,
              priority TEXT,
              due_date TEXT,
              status TEXT)
              ''')  #* execute() method use to query in database
  
  conn.commit()  #* commit() to save all changes to database
  conn.close()
  
def add_task(task, priority, due_date, status="pending"):
  conn = sqlite3.connect(DB_NAME)
  cur = conn.cursor()
  cur.execute('''
              INSERT INTO tasks (task, priority, due_date, status)
              VALUES ( ?, ?, ?, ? )
              ''', ( task, priority, due_date, status ))
  
  conn.commit()
  conn.close()
  
def get_tasks():
  
  