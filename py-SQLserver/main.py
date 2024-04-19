import tkinter as tk
from SQLServerUI import LoginWindow, TableSelectionWindow
from SQLServer import StudentManagementSystem

def main():
    # 创建数据库操作对象
    sms = StudentManagementSystem()
    # 创建登录窗口
    login_window = LoginWindow(on_login_success=lambda: show_table_selection(sms))
    # 进入主循环
    login_window.root.mainloop()

def show_table_selection(sms):
    # 创建表选择窗口，并使用tk.Tk()作为根窗口
    table_selection_root = tk.Tk()
    table_selection_window = TableSelectionWindow(root=table_selection_root, sms=sms)
    # 进入主循环
    table_selection_root.mainloop()

if __name__ == "__main__":
    main()
