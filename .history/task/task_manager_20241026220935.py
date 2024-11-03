from database.database import add_task, get_tasks, delete_task, update_task, move_to_completed


def add_new_task(task, priority, due_date):
  add_task(task, priority, due_date)

def get_all_tasks():
  return get_tasks()

def complete_task(task_id, completed_date) :
  move_to_completed(task_id, completed_date)

def delete_task(task_id):
  delete_task(task_id)

def update_task(task_id, task, priority, due_date):
  update_task(task_id, task, priority, due_date)