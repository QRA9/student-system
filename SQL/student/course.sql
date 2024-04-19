create table student.course
(
    number  varchar(255) not null
        constraint course_pk
            primary key,
    name    varchar(255),
    score   varchar(255),
    time    varchar(255),
    teacher varchar(255)
)
go

