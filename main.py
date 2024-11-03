import tkinter as tk
from task.task_manager import TaskManager
from ui.ui import TaskAppUI

def main():
    # Kết nối cơ sở dữ liệu và khởi tạo các lớp quản lý
    task_manager = TaskManager()
    
    # Khởi tạo cửa sổ Tkinter
    root = tk.Tk()
    
    # Khởi tạo giao diện chính của ứng dụng
    app_ui = TaskAppUI(root, task_manager)
    
    # Chạy ứng dụng
    root.mainloop()

if __name__ == "__main__":
    main()
