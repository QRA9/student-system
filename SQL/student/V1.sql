CREATE VIEW student.V1
As SELECT number,name,sex,major_class,b_day
    FROM student.stu
    WHERE major_class = '电子05'
go

