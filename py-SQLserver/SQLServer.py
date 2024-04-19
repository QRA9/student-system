import pyodbc

def establish_connection():
    try:
        conn_str = 'DRIVER={SQL Server};' \
                   'SERVER=localhost;' \
                   'PORT=1433;' \
                   'DATABASE=student;' \
                   'UID=qhy;' \
                   'PWD=qhy2004'
        conn = pyodbc.connect(conn_str)
        print("成功建立连接。")
        return conn
    except pyodbc.Error as ex:
        sqlstate = ex.args[1]
        print(f"连接到数据库时出错。SQL State: {sqlstate}")
        return None


class StudentManagementSystem:
    def __init__(self):
        self.conn = establish_connection()
        if self.conn:
            self.cursor = self.conn.cursor()

    def close_conn(self):
        if self.conn:
            self.conn.close()
            print("连接已关闭.")

    def get_student_by_id(self, student_id):
        try:
            # 执行查询
            self.cursor.execute("SELECT * FROM student.stu WHERE number=?", (student_id,))

            # 获取查询结果
            student = self.cursor.fetchone()

            if student:
                # 如果找到学生，返回学生信息
                return {
                    'number': student.number,
                    'name': student.name,
                    'sex': student.sex,
                    'major_class': student.major_class,
                    'birthday': student.b_day,
                    'phone_number': student.phone_number
                }
            else:
                # 如果没有找到学生，返回空字典或者其他适当的值
                return {}

        except pyodbc.Error as ex:
            sqlstate = ex.args[1]
            print(f"执行SQL查询时出错。SQL State: {sqlstate}")
            return None

    def query_students(self):
        try:
            self.cursor.execute("SELECT * FROM student.stu")
            students = self.cursor.fetchall()

            # 转换结果为列表字典
            student_list = []
            for student in students:
                student_dict = {
                    'number': student.number,
                    'name': student.name,
                    'sex': student.sex,
                    'major_class': student.major_class,
                    'birthday': student.b_day,
                    'phone_number': student.phone_number
                }
                student_list.append(student_dict)

            return student_list

        except pyodbc.Error as ex:
            sqlstate = ex.args[1]
            print(f"执行SQL查询时出错。SQL State: {sqlstate}")
            return None

    def add_student(self, student_id, name, sex, major, birthdate, phone):
        self.cursor.execute("INSERT INTO student.stu (number, name, sex, major_class, b_day, phone_number) "
                            "VALUES (?, ?, ?, ?, ?, ?)",
                            (student_id, name, sex, major, birthdate, phone))
        self.conn.commit()

    def update_student(self, student_id, name, sex, major, birthdate, phone):
        self.cursor.execute("UPDATE student.stu SET name=?, sex=?, major_class=?, b_day=?, phone_number=? "
                            "WHERE number=?", (name, sex, major, birthdate, phone, student_id))
        self.conn.commit()

    def delete_student(self, student_id):
        self.cursor.execute("DELETE FROM student.stu WHERE number=?", (student_id,))
        self.conn.commit()

    def query_courses(self):
        self.cursor.execute("SELECT * FROM student.course")
        courses = self.cursor.fetchall()
        return courses

    def get_course_by_id(self, course_number):
        try:
            # 执行查询
            self.cursor.execute("SELECT * FROM student.course WHERE number=?", (course_number,))
            # 获取查询结果
            course = self.cursor.fetchone()
            if course:
            # 如果找到课程，返回课程信息
                return {
                    'number': course.number,
                    'name': course.name,
                    'score': course.score,
                    'time': course.time,
                    'teacher': course.teacher
                }
            else:
                # 如果没有找到课程，返回空字典或其他适当的值
                return {}

        except pyodbc.Error as ex:
            sqlstate = ex.args[1]
            print(f"执行SQL查询时出错。SQL State: {sqlstate}")
            return None

    def add_course(self, number, name, score, time, teacher):
        self.cursor.execute("INSERT INTO student.course (number, name, score, time, teacher) VALUES (?, ?, ?, ?, ?)",
                            (number, name, score, time, teacher))
        self.conn.commit()

    def update_course(self, number, name, score, time, teacher):
        self.cursor.execute("UPDATE student.course SET name=?, score=?, time=?, teacher=? WHERE number=?",
                            (name, score, time, teacher, number))
        self.conn.commit()

    def delete_course(self, number):
        self.cursor.execute("DELETE FROM student.course WHERE number=?", (number,))
        self.conn.commit()

    def query_homeworks(self):
        self.cursor.execute("SELECT * FROM student.homework")
        homeworks = self.cursor.fetchall()
        return homeworks

    def get_homework(self, class_number, stu_number):
        try:
            # 执行查询
            self.cursor.execute("SELECT * FROM student.homework WHERE class_number=? AND stu_number=?",
                                (class_number, stu_number))

            # 获取查询结果
            homework = self.cursor.fetchone()

            if homework:
                # 如果找到作业，返回作业信息
                return {
                    'class_number': homework.class_number,
                    'stu_number': homework.stu_number,
                    'score1': homework.score1,
                    'score2': homework.score2,
                    'score3': homework.score3
                }
            else:
                # 如果没有找到作业，返回空字典或其他适当的值
                return {}

        except pyodbc.Error as ex:
            sqlstate = ex.args[1]
            print(f"执行SQL查询时出错。SQL State: {sqlstate}")
            return None

    def add_homework(self, course_number, student_id, exam1, exam2, exam3):
        self.cursor.execute("INSERT INTO student.homework (class_number, stu_number, score1, score2, score3)"
                            " VALUES (?, ?, ?, ?, ?)",
                            (course_number, student_id, exam1, exam2, exam3))
        self.conn.commit()

    def update_homework(self, course_number, student_id, exam1, exam2, exam3):
        self.cursor.execute("UPDATE student.homework SET score1=?, score2=?, score3=? WHERE class_number=? "
                            "AND stu_number=?",
                            (exam1, exam2, exam3, course_number, student_id))
        self.conn.commit()

    def delete_homework(self, course_number, student_id):
        self.cursor.execute("DELETE FROM student.homework WHERE class_number=? AND stu_number=?",
                            (course_number, student_id))
        self.conn.commit()


