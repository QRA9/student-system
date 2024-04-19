import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class LoginWindow:
    def __init__(self, on_login_success):
        self.on_login_success = on_login_success
        self.root = tk.Tk()
        self.root.title("登录界面")

        ttk.Label(self.root, text="用户名:").grid(row=0, column=0, padx=5, pady=5, sticky="E")
        ttk.Label(self.root, text="密码:").grid(row=1, column=0, padx=5, pady=5, sticky="E")

        self.username = ttk.Entry(self.root)
        self.username.grid(row=0, column=1, padx=5, pady=5)
        self.password = ttk.Entry(self.root, show="*")
        self.password.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(self.root, text="登录", command=self.login).grid(row=2, column=0, columnspan=2, pady=10)

    def login(self):
        if self.check_credentials():
            self.root.destroy()
            self.on_login_success()
        else:
            messagebox.showerror("登录失败", "用户名或密码错误")

    def check_credentials(self):
        return self.username.get() == "qhy" and self.password.get() == "2004"

class TableSelectionWindow:
    def __init__(self, root, sms):
        self.root = root
        self.sms = sms
        self.root.title("表选择")

        ttk.Label(self.root, text="请选择要操作的表：").grid(row=0, column=0, padx=5, pady=5)

        self.table_combobox = ttk.Combobox(self.root, values=["学生表", "课程表", "作业表"])
        self.table_combobox.grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(self.root, text="确认", command=self.open_table_management).grid(row=1, column=0, columnspan=2, pady=10)

    def open_table_management(self):
        selected_table = self.table_combobox.get()
        if selected_table == "学生表":
            student_app = StudentManagementApp(self.root, self.sms)
            student_app.root.mainloop()
        elif selected_table == "课程表":
            course_app = CourseManagementApp(self.root, self.sms)
            course_app.root.mainloop()
        elif selected_table == "作业表":
            homework_app = HomeworkManagementApp(self.root, self.sms)
            homework_app.root.mainloop()

class StudentManagementApp:
    def __init__(self, root, sms):
        self.del_stu_id = None
        self.new_phone = None
        self.new_birthday = None
        self.new_major = None
        self.new_sex = None
        self.new_name = None
        self.new_stu_id = None
        self.root = tk.Toplevel(root)
        self.sms = sms
        self.root.title("学生管理")
        self.root.geometry("600x400")

        # 创建标签
        self.label = ttk.Label(self.root, text="学号:")
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky="E")

        # 创建输入框
        self.input_id = ttk.Entry(self.root)
        self.input_id.grid(row=0, column=1, padx=5, pady=5)

        # 创建按钮
        self.query_button = ttk.Button(self.root, text="查询学生", command=self.query_student)
        self.query_button.grid(row=0, column=2, padx=5, pady=5)

        self.add_button = ttk.Button(self.root, text="增加学生", command=self.open_add_student_window)
        self.add_button.grid(row=1, column=0, padx=5, pady=5)

        self.update_button = ttk.Button(self.root, text="更新学生", command=self.update_student)
        self.update_button.grid(row=1, column=1, padx=5, pady=5)

        self.delete_button = ttk.Button(self.root, text="删除学生", command=self.open_del_student)
        self.delete_button.grid(row=1, column=2, padx=5, pady=5)

        # 创建列表框用于显示学生信息
        self.student_listbox = tk.Listbox(self.root, height=10, width=60)
        self.student_listbox.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

        self.clear_list()

    def query_student(self):
        student_id = self.input_id.get()
        if not student_id:
            messagebox.showwarning("错误", "请输入学号")
            return

        stu_all = self.sms.get_student_by_id(student_id)

        if stu_all:
            messagebox.showinfo("查询结果",
                                f"学号: {stu_all['number']}\n姓名: {stu_all['name']}\n性别: {stu_all['sex']}\n"
                                f"专业班级: {stu_all['major_class']}\n出生日期: {stu_all['birthday']}\n"
                                f"联系电话: {stu_all['phone_number']}")
        else:
            messagebox.showinfo("查询结果", "未找到该学生")

    def open_add_student_window(self):
        add_new = tk.Toplevel(self.root)
        add_new.title("添加学生")

        ttk.Label(add_new, text="学号:").grid(row=0, column=0, padx=5, pady=5, sticky="E")
        ttk.Label(add_new, text="姓名:").grid(row=1, column=0, padx=5, pady=5, sticky="E")
        ttk.Label(add_new, text="性别:").grid(row=2, column=0, padx=5, pady=5, sticky="E")
        ttk.Label(add_new, text="专业班级:").grid(row=3, column=0, padx=5, pady=5, sticky="E")
        ttk.Label(add_new, text="出生日期:").grid(row=4, column=0, padx=5, pady=5, sticky="E")
        ttk.Label(add_new, text="联系电话:").grid(row=5, column=0, padx=5, pady=5, sticky="E")

        self.new_stu_id = ttk.Entry(add_new)
        self.new_stu_id.grid(row=0, column=1, padx=5, pady=5)
        self.new_name = ttk.Entry(add_new)
        self.new_name.grid(row=1, column=1, padx=5, pady=5)
        self.new_sex = ttk.Entry(add_new)
        self.new_sex.grid(row=2, column=1, padx=5, pady=5)
        self.new_major = ttk.Entry(add_new)
        self.new_major.grid(row=3, column=1, padx=5, pady=5)
        self.new_birthday = ttk.Entry(add_new)
        self.new_birthday.grid(row=4, column=1, padx=5, pady=5)
        self.new_phone = ttk.Entry(add_new)
        self.new_phone.grid(row=5, column=1, padx=5, pady=5)

        ttk.Button(add_new, text="确认添加", command=self.add_student).grid(row=6, column=0, columnspan=2, pady=10)

    def add_student(self):
        student_id = self.new_stu_id.get()
        if not student_id:
            messagebox.showwarning("错误", "请输入学号")
            return

        name = self.new_name.get()
        sex = self.new_sex.get()
        major = self.new_major.get()
        birthday = self.new_birthday.get()
        phone_number = self.new_phone.get()

        self.sms.add_student(student_id, name, sex, major, birthday, phone_number)
        messagebox.showinfo("操作结果", "成功添加学生")
        self.child_close()

    def open_del_student(self):
        del_stu = tk.Toplevel(self.root)
        del_stu.title("删除学生")

        ttk.Label(del_stu, text="学号:").grid(row=0, column=0, padx=5, pady=5, sticky="E")
        self.del_stu_id = ttk.Entry(del_stu)
        self.del_stu_id.grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(del_stu, text="确认删除", command=self.delete_student).grid(row=1, column=0, columnspan=2, pady=10)

    def delete_student(self):
        student_id = self.del_stu_id.get()
        if not student_id:
            messagebox.showwarning("错误", "请输入学号")
            return

        if not self.sms.get_student_by_id(student_id):
            messagebox.showinfo("操作结果", "该学生不存在")
        else:
            self.sms.delete_student(student_id)
            messagebox.showinfo("操作结果", "成功删除学生")
            self.child_close()

    def child_close(self):
        # 处理子窗口关闭
        self.clear_list()

    def update_student(self):
        student_id = self.input_id.get()
        name = "修改后的姓名"
        sex = "修改后的性别"
        major_class = "修改后的专业班级"
        birthday = "修改后的出生日期"
        phone_number = "修改后的联系电话"
        self.sms.update_student(student_id, name, sex, major_class, birthday, phone_number)
        messagebox.showinfo("操作结果", "成功更新学生信息")
        self.clear_list()

    def clear_list(self):
        # 清空列表框
        self.student_listbox.delete(0, tk.END)

        # 查询所有学生信息
        students = self.sms.query_students()

        # 将学生信息添加到列表框
        for student in students:
            self.student_listbox.insert(tk.END, f"{student['number']} - {student['name']} - {student['sex']} - "
                                                f"{student['major_class']} - {student['birthday']} - "
                                                f"{student['phone_number']}")


class CourseManagementApp:
    def __init__(self, root, sms):
        self.delete_cou_id_entry = None
        self.new_cou_teacher_entry = None
        self.new_cou_time_entry = None
        self.new_cou_score_entry = None
        self.new_cou_name_entry = None
        self.new_cou_id_entry = None
        self.root = tk.Toplevel(root)
        self.sms = sms
        self.root.title("课程管理")

        # 创建标签
        self.label = ttk.Label(self.root, text="课程编号:")
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky="E")

        # 创建输入框
        self.course_id_entry = ttk.Entry(self.root)
        self.course_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # 创建按钮
        self.query_button = ttk.Button(self.root, text="查询课程", command=self.query_course)
        self.query_button.grid(row=0, column=2, padx=5, pady=5)

        self.add_button = ttk.Button(self.root, text="增加课程", command=self.open_add_course_window)
        self.add_button.grid(row=1, column=0, padx=5, pady=5)

        self.update_button = ttk.Button(self.root, text="更新课程", command=self.update_course)
        self.update_button.grid(row=1, column=1, padx=5, pady=5)

        self.delete_button = ttk.Button(self.root, text="删除课程", command=self.open_delete_course_window)
        self.delete_button.grid(row=1, column=2, padx=5, pady=5)

        # 创建列表框用于显示课程信息
        self.course_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, height=10, width=60)
        self.course_listbox.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

        # 刷新课程列表
        self.refresh_course_list()

    def query_course(self):
        course_id = self.course_id_entry.get()
        if not course_id:
            messagebox.showwarning("错误", "请输入课程编号")
            return

        course_info = self.sms.get_course_by_id(course_id)

        if course_info:
            messagebox.showinfo("查询结果",
                                f"课程编号: {course_info['number']}\n课程名称: {course_info['name']}\n学分: {course_info['score']}\n"
                                f"时间: {course_info['time']}\n授课教师: {course_info['teacher']}")
        else:
            messagebox.showinfo("查询结果", "未找到该课程")

    def open_add_course_window(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("添加课程")

        ttk.Label(add_window, text="课程编号:").grid(row=0, column=0, padx=5, pady=5, sticky="E")
        ttk.Label(add_window, text="课程名称:").grid(row=1, column=0, padx=5, pady=5, sticky="E")
        ttk.Label(add_window, text="学分:").grid(row=2, column=0, padx=5, pady=5, sticky="E")
        ttk.Label(add_window, text="时间:").grid(row=3, column=0, padx=5, pady=5, sticky="E")
        ttk.Label(add_window, text="授课教师:").grid(row=4, column=0, padx=5, pady=5, sticky="E")

        self.new_cou_id_entry = ttk.Entry(add_window)
        self.new_cou_id_entry.grid(row=0, column=1, padx=5, pady=5)
        self.new_cou_name_entry = ttk.Entry(add_window)
        self.new_cou_name_entry.grid(row=1, column=1, padx=5, pady=5)
        self.new_cou_score_entry = ttk.Entry(add_window)
        self.new_cou_score_entry.grid(row=2, column=1, padx=5, pady=5)
        self.new_cou_time_entry = ttk.Entry(add_window)
        self.new_cou_time_entry.grid(row=3, column=1, padx=5, pady=5)
        self.new_cou_teacher_entry = ttk.Entry(add_window)
        self.new_cou_teacher_entry.grid(row=4, column=1, padx=5, pady=5)

        ttk.Button(add_window, text="确认添加", command=self.add_course).grid(row=5, column=0, columnspan=2, pady=10)

    def add_course(self):
        course_id = self.new_cou_id_entry.get()
        if not course_id:
            messagebox.showwarning("错误", "请输入课程编号")
            return

        name = self.new_cou_name_entry.get()
        score = self.new_cou_score_entry.get()
        time = self.new_cou_time_entry.get()
        teacher = self.new_cou_teacher_entry.get()

        self.sms.add_course(course_id, name, score, time, teacher)
        messagebox.showinfo("操作结果", "成功添加课程")
        self.on_child_closing()

    def open_delete_course_window(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("删除课程")

        ttk.Label(delete_window, text="课程编号:").grid(row=0, column=0, padx=5, pady=5, sticky="E")
        self.delete_cou_id_entry = ttk.Entry(delete_window)
        self.delete_cou_id_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(delete_window, text="确认删除", command=self.delete_course).grid(row=1, column=0, columnspan=2, pady=10)

    def delete_course(self):
        course_id = self.delete_cou_id_entry.get()
        if not course_id:
            messagebox.showwarning("错误", "请输入课程编号")
            return

        if not self.sms.get_course_by_id(course_id):
            messagebox.showinfo("操作结果", "该课程不存在")
        else:
            self.sms.delete_course(course_id)
            messagebox.showinfo("操作结果", "成功删除课程")
            self.on_child_closing()

    def on_child_closing(self):
        # 处理子窗口关闭
        self.refresh_course_list()

    def update_course(self):
        course_id = self.course_id_entry.get()
        name = "修改后的课程名称"
        score = "修改后的学分"
        time = "修改后的时间"
        teacher = "修改后的授课教师"

        self.sms.update_course(course_id, name, score, time, teacher)
        messagebox.showinfo("操作结果", "成功更新课程信息")
        self.refresh_course_list()

    def refresh_course_list(self):
        # 清空列表框
        self.course_listbox.delete(0, tk.END)

        # 查询所有课程信息
        courses = self.sms.query_courses()

        # 将课程信息添加到列表框
        for course in courses:
            self.course_listbox.insert(tk.END, f"number:{course[0]} - name:{course[1]}")

class HomeworkManagementApp:
    def __init__(self, root, sms):
        self.root = tk.Toplevel(root)
        self.sms = sms
        self.root.title("作业管理")

        # 创建标签
        self.label_course = ttk.Label(self.root, text="课程编号:")
        self.label_course.grid(row=0, column=0, padx=5, pady=5, sticky="E")

        self.label_student = ttk.Label(self.root, text="学生学号:")
        self.label_student.grid(row=1, column=0, padx=5, pady=5, sticky="E")

        # 创建输入框
        self.course_id_entry = ttk.Entry(self.root)
        self.course_id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.student_id_entry = ttk.Entry(self.root)
        self.student_id_entry.grid(row=1, column=1, padx=5, pady=5)

        # 创建按钮
        self.query_button = ttk.Button(self.root, text="查询作业", command=self.query_homework)
        self.query_button.grid(row=0, column=2, padx=5, pady=5, rowspan=2)

        self.add_button = ttk.Button(self.root, text="增加作业", command=self.open_add_homework_window)
        self.add_button.grid(row=2, column=0, padx=5, pady=5)

        self.update_button = ttk.Button(self.root, text="更新作业", command=self.update_homework)
        self.update_button.grid(row=2, column=1, padx=5, pady=5)

        self.delete_button = ttk.Button(self.root, text="删除作业", command=self.open_delete_homework_window)
        self.delete_button.grid(row=2, column=2, padx=5, pady=5)

        # 创建列表框用于显示作业信息
        self.homework_listbox = tk.Listbox(self.root, height=10, width=60)
        self.homework_listbox.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

        # 刷新作业列表
        self.refresh_homework_list()

    def query_homework(self):
        course_id = self.course_id_entry.get()
        student_id = self.student_id_entry.get()

        if not course_id or not student_id:
            messagebox.showwarning("错误", "请输入课程编号和学生学号")
            return

        homework_info = self.sms.get_homework(course_id, student_id)

        if homework_info:
            messagebox.showinfo("查询结果",
                                f"课程编号: {homework_info['class_number']}\n学生学号: {homework_info['stu_number']}\n"
                                f"考试1成绩: {homework_info['score1']}\n考试2成绩: {homework_info['score2']}\n"
                                f"考试3成绩: {homework_info['score3']}")
        else:
            messagebox.showinfo("查询结果", "未找到该学生在该课程的作业")

    def open_add_homework_window(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("添加作业")

        ttk.Label(add_window, text="课程编号:").grid(row=0, column=0, padx=5, pady=5, sticky="E")
        ttk.Label(add_window, text="学生学号:").grid(row=1, column=0, padx=5, pady=5, sticky="E")
        ttk.Label(add_window, text="考试1成绩:").grid(row=2, column=0, padx=5, pady=5, sticky="E")
        ttk.Label(add_window, text="考试2成绩:").grid(row=3, column=0, padx=5, pady=5, sticky="E")
        ttk.Label(add_window, text="考试3成绩:").grid(row=4, column=0, padx=5, pady=5, sticky="E")

        self.new_course_id_entry = ttk.Entry(add_window)
        self.new_course_id_entry.grid(row=0, column=1, padx=5, pady=5)
        self.new_student_id_entry = ttk.Entry(add_window)
        self.new_student_id_entry.grid(row=1, column=1, padx=5, pady=5)
        self.new_score1_entry = ttk.Entry(add_window)
        self.new_score1_entry.grid(row=2, column=1, padx=5, pady=5)
        self.new_score2_entry = ttk.Entry(add_window)
        self.new_score2_entry.grid(row=3, column=1, padx=5, pady=5)
        self.new_score3_entry = ttk.Entry(add_window)
        self.new_score3_entry.grid(row=4, column=1, padx=5, pady=5)

        ttk.Button(add_window, text="确认添加", command=self.add_homework).grid(row=5, column=0, columnspan=2, pady=10)

    def add_homework(self):
        course_id = self.new_course_id_entry.get()
        student_id = self.new_student_id_entry.get()
        score1 = self.new_score1_entry.get()
        score2 = self.new_score2_entry.get()
        score3 = self.new_score3_entry.get()

        if not course_id or not student_id:
            messagebox.showwarning("错误", "请输入课程编号和学生学号")
            return

        self.sms.add_homework(course_id, student_id, score1, score2, score3)
        messagebox.showinfo("操作结果", "成功添加作业")
        self.on_child_closing()

    def open_delete_homework_window(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("删除作业")

        ttk.Label(delete_window, text="课程编号:").grid(row=0, column=0, padx=5, pady=5, sticky="E")
        ttk.Label(delete_window, text="学生学号:").grid(row=1, column=0, padx=5, pady=5, sticky="E")

        self.delete_course_id_entry = ttk.Entry(delete_window)
        self.delete_course_id_entry.grid(row=0, column=1, padx=5, pady=5)
        self.delete_student_id_entry = ttk.Entry(delete_window)
        self.delete_student_id_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(delete_window, text="确认删除", command=self.delete_homework).grid(row=2, column=0, columnspan=2, pady=10)

    def delete_homework(self):
        course_id = self.delete_course_id_entry.get()
        student_id = self.delete_student_id_entry.get()

        if not course_id or not student_id:
            messagebox.showwarning("错误", "请输入课程编号和学生学号")
            return

        if not self.sms.get_homework(course_id, student_id):
            messagebox.showinfo("操作结果", "该学生在该课程没有作业记录")
        else:
            self.sms.delete_homework(course_id, student_id)
            messagebox.showinfo("操作结果", "成功删除作业记录")
            self.on_child_closing()

    def update_homework(self):
        course_id = self.course_id_entry.get()
        student_id = self.student_id_entry.get()
        score1 = "修改后的考试1成绩"
        score2 = "修改后的考试2成绩"
        score3 = "修改后的考试3成绩"

        self.sms.update_homework(course_id, student_id, score1, score2, score3)
        messagebox.showinfo("操作结果", "成功更新作业信息")
        self.refresh_homework_list()

    def refresh_homework_list(self):
        # 清空列表框
        self.homework_listbox.delete(0, tk.END)
        # 查询所有作业信息
        homeworks = self.sms.query_homeworks()
        # 将作业信息添加到列表框
        for homework in homeworks:
            print(homework)
            self.homework_listbox.insert(0, f"class_number:{homework[0]} - stu_number:{homework[1]}")

