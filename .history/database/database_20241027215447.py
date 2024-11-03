import sqlite3
from datetime import datetime
DB_NAME = "todo_list.db"

class Database:
  conn = sqlite3.connect(DB_NAME)  #* Connect to the database
  
  def __init__(self):
    
  def connect_db():
    cur = conn.cursor()  #* We using this to manipulate with query in database
    cur.execute('''
                CREATE TABLE IF NOT EXISTS tasks
                (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                priority TEXT,
                due_date TEXT,
                status TEXT
                )
                ''')  #* execute() method use to query in database

    cur.execute(
      '''
                CREATE TABLE IF NOT EXISTS completed_tasks
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                priority TEXT,
                due_date TEXT,
                completed_date TEXT)
      '''
    )
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

  def move_to_completed(task_id, completed_date):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT task, priority, due_date FROM tasks WHERE id=?", (task_id,))
    task = cur.fetchone()

    if task:
      cur.execute("INSERT INTO completed_tasks(task, priority, due_date, completed_date) VALUES (?, ?, ?, ?)", (task[0], task[1], task[2],  completed_date))
      cur.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()

  def get_tasks():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()  #* Retrieve all rows of a query result as a list of tuples
    conn.close()
    return tasks

  def delete_task(task_id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id=?", (task_id, ))
    conn.commit()
    conn.close()

  def update_task(task_id, task, priority, due_date):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET task=?, priority=?, due_date=? WHERE id=?", ( task, priority, due_date, task_id ))
    conn.commit()
    conn.close()

  def get_all_tasks():
    return 