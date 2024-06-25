import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()

cur.execute(
    """CREATE TABLE IF NOT EXISTS student(id int primary key,name varchar(250),dob date);"""
)
cur.execute(
    """CREATE TABLE IF NOT EXISTS teacher(employee_id int primary key,name varchar(250),age int,doj date);"""
)


def insert_student(student_name, student_dob):
    query = "INSERT INTO student(name,dob)VALUES (?,?)"
    cur.execute(query, (student_name, student_dob))
    print("student Inserted successfully")


while True:
    user_input = int(input("1.CREATE\n2.READ\n3.UPDATE\n4.DELETE\n"))

    if user_input == 1:
        student_name = input("Enter name:")
        student_dob = input("Enter date of birth:")
        insert_student(student_name, student_dob)
