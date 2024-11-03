import sqlite3

DB_NAME = "todo_list.db"

def connect_db():
  conn = sqlite3.connect(DB_NAME)
  