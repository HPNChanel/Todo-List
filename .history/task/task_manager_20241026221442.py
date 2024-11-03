from database.database import add_task, get_tasks, delete_task as db_delete_task, move_to_completed


def add_new_task(task, priority, due_date):
  add_task(task, priority, due_date)

def get_all_tasks():
  return get_tasks()

def complete_task(task_id, completed_date) :
  move_to_completed(task_id, completed_date)

def remove_task(task_id):
  db_delete_task(task_id)

def edit_task(task_id, task, priority, due_date):
  edit_task(task_id, task, priority, due_date)