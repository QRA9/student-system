CREATE VIEW student.V2
AS SELECT stu_number, stu.name, class_number, score1, score2, score3
FROM student.homework,student.stu,student.course
WHERE (major_class = '生物05') AND (stu.number = stu_number) AND (class_number = course.number)
go

