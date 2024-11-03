from database.database import add_task, get_tasks, update_task_status, delete_task


def add_new_task(task, priority, due_date):
  add_task(task, priority, due_date)

def get_all_tasks():
  return get_tasks()

def complete_task(task_id):
  update_task_status(task_id, )