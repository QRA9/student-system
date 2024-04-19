create table student.stu
(
    number       varchar(255) not null
        constraint stu_pk
            primary key,
    name         varchar(255),
    sex          varchar(255),
    major_class  varchar(255),
    b_day        varchar(255),
    phone_number varchar(255)
)
go

