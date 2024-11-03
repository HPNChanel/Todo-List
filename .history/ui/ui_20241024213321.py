import tkinter as tk
from tkinter import messagebox
from task.task_manager import add_new_task, get_all_tasks, complete_task
from ui.forms import TaskForm

def create_ui():
  root = tk.Tk()  #* Tk(): constructor method used to create the main application window
  root.title("Todo List")
  
  #* Frame for display task list
  task_listbox = tk.Listbox(root, height=10, width=50)  #* Listbox() is used to create a list of items from which a user can select one or more
  task_listbox.pack()
  
  #* Add a new task 
  def add_task_ui():
    form = TaskForm(root, add_new_task)
    form.show()
  
  add_button = tk.Button(root, text="Add Task", command=add_task_ui)
  add_button.pack()
  

  
  root.mainloop()