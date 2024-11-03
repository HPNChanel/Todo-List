from datetime import datetime
from database.database import Database

class TaskManager:
  def __init__(self):
    self.database = Database()
    
  def add_new_task(self, task, priority, due_date):
    self.database.add_task(task, priority, due_date)

  def get_all_tasks(self):
    return self.database.get_tasks()

  def complete_task(self, task_id):
    completed_date = datetime.now()
    move_to_completed(task_id, completed_date)

  def remove_task(self, task_id):
    db_delete_task(task_id)

  def edit_task(self, task_id, task, priority, due_date):
    edit_task(task_id, task, priority, due_date)