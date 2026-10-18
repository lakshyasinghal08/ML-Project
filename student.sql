create database college
use college

CREATE TABLE Student (
    id INT IDENTITY(1,1) PRIMARY KEY,
    gender VARCHAR(20),
    race_ethnicity VARCHAR(50),
    parental_level_of_education VARCHAR(100),
    lunch VARCHAR(50),
    test_preparation_course VARCHAR(50),
    math_score INT,
    reading_score INT,
    writing_score INT
);
select * from Student;