import tkinter as tk
from tkinter import ttk
from ui.task_table import TaskTable
from task.task_manager import add_new_task, get_all_tasks, complete_task, delete_task
from ui.task_table import 

def create_ui():
  root = tk.Tk()  #* Tk(): constructor method used to create the main application window
  root.title("Todo List")
  
  task_table = TaskTable(root)
  task_table.pack()
  
  #* Add a new task 
  def add_task_ui():
    form = TaskForm(root, add_new_task)
    form.show()
  
  add_button = tk.Button(root, text="Add Task", command=add_task_ui)
  add_button.pack()
  

  
  root.mainloop()